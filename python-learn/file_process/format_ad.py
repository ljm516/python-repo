import codecs
import json

import sys


class Advertise(object):
    def __init__(self, title, category, desc1, desc2, url):
        self.title = title
        self.category = category
        self.desc1 = desc1
        self.desc2 = desc2
        self.url = url


def format_function(file_name):

    file_path = 'file_path\\'

    d = {}
    with codecs.open(file_path + file_name + '.txt', 'r', encoding='utf-8') as inputFile:

        for line in inputFile:
            lines_part = line.split("\t")
            ad = Advertise

            ad.category = lines_part[0]
            ad.title = lines_part[1]
            ad.desc1 = lines_part[2]
            ad.desc2 = lines_part[3]
            ad.url = lines_part[4].replace("\r", "").replace("\n", "")

            if ad.category in d.keys():
                d.get(ad.category).append(object_to_json(ad))
            else:
                ad_list = []
                ad_list.append(object_to_json(ad))
                d[ad.category] = ad_list

    for k in d.keys():
        print(k, ": ", len(d[k]))

    with codecs.open(file_path + file_name + '.json', 'w', encoding='UTF-8') as outputJsonFile:
        json.dump(d, outputJsonFile, indent=4, ensure_ascii=False)


def object_to_json(ad):
    return {
        "category": ad.category,
        "title": ad.title,
        "desc1": ad.desc1,
        "desc2": ad.desc2,
        "url": ad.url
    }


if __name__ == '__main__':

    format_function(sys.argv[1])
