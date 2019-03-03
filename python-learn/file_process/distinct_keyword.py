import codecs


def distinct_function():

    file_path = 'file_path\\'

    with codecs.open(file_path + 'all_keyword.txt', 'r', "UTF-8") as inputFile:

        list = []
        times = 0
        similar_count = 0
        for line in inputFile:
            times += 1
            if line is not "" and line not in list:
                list.append(line)
            else:
                similar_count += 1
                print("相同的keyword: " + line, " ", similar_count)

        print("总词数: ", times)
        print("去重之后的次数:", len(list))

    with open(file_path + 'all_keyword.txt', 'w', encoding='UTF-8') as outputFile:
        s = ''
        for item in list:
            format_item = item.replace("\r\n", "\n")
            s += format_item

        outputFile.write(s)


distinct_function()
