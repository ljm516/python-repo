from pyexcel_xlsx import save_data, get_data
from collections import OrderedDict
import json

file_path = 'D:\\lijiangming\\docs\\python-third_libs\\excel_lib\\test.xlsx'

def write_xlsx():
	data = OrderedDict()
	data.update({'sheet_1': [[1, 2, 3], [4, 5, 6]]})
	data.update({'sheet_2': [['row1', '嘿嘿', '123']]})

	save_data(file_path, data)


def read_xlsx():
	data = get_data(file_path)
	print(json.dumps(data, ensure_ascii=False))


read_xlsx()