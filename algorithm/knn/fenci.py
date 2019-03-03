import sys
import codecs
import jieba

'''
	训练语言模型，将语料库中的文章分词
'''

if __name__ == '__main__':
	input_file = sys.argv[1]
	output_file = sys.argv[2]

	input_reader = codecs.open(input_file, 'r', encoding='utf-8')
	out_writer = codecs.open(output_file, 'w', encoding='utf-8')
	
	line = input_reader.readline()
	line_num = 1
	while line:
		print('processing line: {l} article...'.format(l=line_num))
		seg_list = jieba.cut(line, cut_all=False)
		line_seg = ' '.join(seg_list)
		out_writer.writelines(line_seg)
		line_num += 1
		line = input_reader.readline()

	print('all done...')
	input_reader.close()
	out_writer.close()
