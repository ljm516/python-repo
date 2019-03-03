import re
import sys

import os
from bs4 import BeautifulSoup


def get_content_from_file(file_path):
    content = ''
    with open(file_path, 'r', encoding='utf-8') as content_file:
        for i, v in enumerate(content_file.readlines()):
            if i == 0 or i == 1:
                continue
            content += v.strip()

    return content


def get_content_list(content_dir):
    content_list = []
    for file in os.listdir(content_dir):
        file_path = os.path.join(content_dir, file)
        if not os.path.isdir(file_path):
            content_list.append(get_content_from_file(file_path=file_path))

    return content_list


if __name__ == '__main__':
    content_dir = sys.argv[1]
    corpus_file = sys.argv[2]

    content_list = get_content_list(content_dir=content_dir)
    writer = open(corpus_file, 'w', encoding='utf-8')
    for content in content_list:
        content_text_tag = BeautifulSoup(content)
        script_tag = content_text_tag.find_all(name='script')
        style_tag = content_text_tag.find_all(name='style')
        if len(script_tag) != 0:
            for tag in script_tag:
                tag.decompose()
        else:
            print('no script tag')

        if len(style_tag) != 0:
            for tag in style_tag:
                tag.decompose()
        else:
            print('not style tag')

        content_text = content_text_tag.get_text()
        content_text = re.sub(
            "[\s+\.\!\/_,$%^*(+\"\'；：“”．]+|[+——！，。？?、~@#￥%……&*（ ）《 》 ’ ‘ 「 」 - ) | ・ ✦ ｜]+", "", content_text)

        writer.write(content_text + '\n')

    writer.close()
