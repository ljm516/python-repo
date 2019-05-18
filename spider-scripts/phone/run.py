import sys
import xlrd
import time
import phone.spider as spider


def run(excel_file):
    excel_data = xlrd.open_workbook(excel_file)

    sheet_list = excel_data.sheets()

    result_dict = {}
    count = 0
    for sheet in sheet_list:
        rows = sheet.nrows
        for i in range(rows):
            if i == 0:
                continue
            row_value_list = sheet.row_values(i)
            phone = int(row_value_list[0])

            if str(phone).startswith("170") or str(phone).startswith("171"):
                operator = spider.crawling(phone)
                result_dict[phone] = operator
                count += 1
                if count % 50 == 0:
                    print('睡眠3s')
                    time.sleep(3)

    return result_dict


if __name__ == '__main__':
    print("process start...")
    source_file = sys.argv[1]

    result = run(source_file)

    with open("phone_operator.txt", 'w', encoding='utf-8') as f:
        for key in result.keys():
            f.write(str(key) + '\t' + result[key] + '\n')
