import sys
import os
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from models import Article


def get_article_list(file_dir):
    article_list = []
    for file in os.listdir(file_dir):
        file_path = os.path.join(file_dir, file)

        if not os.path.isdir(file_path):
            a = Article()
            content = ''
            with open(file_path, 'r', encoding='utf-8') as file_reader:
                for line in file_reader.readlines():
                    content += line.strip()

            a.title = file[:-4]
            a.content = content

            article_list.append(a)

    return article_list


def create_result_dir(base_dir):
    result_dir = base_dir + '/tfidf_result/'
    if not os.path.isdir(result_dir):
        os.mkdir(result_dir)

    return result_dir


# 计算 tf-idf
def cal_tf_idf(data):
    # 将文章分词
    word_list = jieba.lcut(data)

    # 将得到的词语转换为词频矩阵
    fre_word = CountVectorizer()

    # 统计每个词语的 tf-idf 权值
    transformer = TfidfTransformer()

    # 计算出 tf-idf，并将其转化为 tf-idf 矩阵
    tf_idf = transformer.fit_transform(fre_word.fit_transform(word_list))

    # 获取词袋模型中的所有词语
    word = fre_word.get_feature_names()

    # 获取权重
    weight = tf_idf.toarray()

    tfidf_dict = {}
    for i in range(len(weight)):
        for j in range(len(word)):
            get_word = word[j]
            get_value = weight[i][j]
            if get_value != 0:
                if get_word in tfidf_dict.keys():
                    tfidf_dict[get_word] += float(get_value)
                else:
                    tfidf_dict.update({get_word: get_value})

    sorted_tfidf = sorted(tfidf_dict.items(), key=lambda d: d[1], reverse=True)

    return sorted_tfidf


if __name__ == '__main__':
    file_dir = sys.argv[1]
    article_list = get_article_list(file_dir=file_dir)
    print('article list size: {s}'.format(s=len(article_list)))

    result_dir = create_result_dir(base_dir=file_dir)
    for article in article_list:
        print('current article: {a}'.format(a=article.title))
        article_tfidf = cal_tf_idf(data=article.content)
        article_tfidf_result_file = result_dir + article.title + '.txt'
        with open(article_tfidf_result_file, 'w', encoding='utf-8') as result:
            for tfidf in article_tfidf:
                result.write('{0}\t{1}\n'.format(tfidf[0], tfidf[1]))
