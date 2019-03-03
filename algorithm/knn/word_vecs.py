import sys
import logging

import gensim
import codecs
import numpy as np
import jieba
import re
import pandas as pd

'''
    语句向量生成
'''


def get_word_vecs(word_list, model):
    vecs = []
    for word in word_list:
        try:
            vecs.append(model[word])
        except KeyError as e:
            continue

    return np.array(vecs, dtype='float')


def build_vecs(file_path, model):
    file_vecs = []
    with codecs.open(file_path, 'r', encoding='utf-8') as contents:
        for line in contents:
            line = line.strip()
            line_array = line.split('\t')
            type_value = float(line_array[0])
            sentence = line_array[1]

            sentence = re.sub(
                "[\s+\.\!\/_,$%^*(+\"\'；：“”．]+|[+——！，。？?、~@#￥%……&*（）]+", "", sentence)

            word_list = jieba.lcut(sentence)
            print('word_list: {wl}'.format(wl=word_list))
            vecs = get_word_vecs(word_list=word_list, model=model)
            if len(vecs) > 0:

                sum_vecs = sum(np.array(vecs))
                vecs_length = len(vecs)
                vecs_array = sum_vecs / vecs_length
            
                vecs_list = vecs_array.tolist()
                vecs_list.append(type_value) 

                vecs_array = np.array(vecs_list)   

                print('vecs shape: {s}'.format(s=vecs.shape))
                print('vecs array: {sum}'.format(sum=vecs_array))
                print('vecs length: {l}'.format(l=vecs_length))
                print('vecs_array shape: {va}'.format(va=vecs_array.shape))
                
                file_vecs.append(vecs_array)

    return file_vecs


if __name__ == '__main__':
    program_name = sys.argv[0]
    logger = logging.getLogger(name=program_name)

    logging.basicConfig(format=('%(asctime)s: %(levelname)s: %(message)s'))
    logging.root.setLevel(level=logging.INFO)
    logger.info('running {s}'.format(s=' '.join(sys.argv)))

    input_file = sys.argv[1]
    model = gensim.models.KeyedVectors.load_word2vec_format(
        input_file, binary=False)

    sentence_file = sys.argv[2]
    result = build_vecs(file_path=sentence_file, model=model)
    # np_data = np.array(result)
    # pd_data = pd.DataFrame(np_data)

    # print('pd_data: {pd}'.format(pd=pd_data))

    result_csv_file = sys.argv[3]
    # pd_data.to_csv(result_csv_file)
    np.savetxt(result_csv_file, result, delimiter=',')
