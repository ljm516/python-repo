from openpyxl import load_workbook

file_path = 'D:\\lijiangming\\docs\\python-third_libs\\excel_lib\\test.xlsx'

def read_excel():
	wb = load_workbook(file_path)
	sheet_names = wb.get_sheet_names()
	content = []
	for name in sheet_names:
		print(name)
		ws = wb.get_sheet_by_name(name)

		rows = ws.rows
		columns = ws.columns

		
		for row in rows:
			line = [col.value for col in row]
			content.append(line)

	print(content)
read_excel()


