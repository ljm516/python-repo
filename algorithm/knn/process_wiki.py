import sys
import logging

from gensim.corpora import WikiCorpus

'''
	将维基百科里的语料库处理成text格式的文件
'''

if __name__ == '__main__':
	program_name = sys.argv[0]
	logger = logging.getLogger(name=program_name)

	logging.basicConfig(format=('%(asctime)s: %(levelname)s: %(message)s'))
	logging.root.setLevel(level=logging.INFO)
	logger.info('running {s}'.format(s=','.join(sys.argv)))

	if len(sys.argv) < 3:
		logging.info('please input source file ang target file...')
		exit(-1)

	input_file = sys.argv[1]
	output_file = sys.argv[2]
	space = ' '
	i = 0

	out = open(output_file, 'w', encoding='utf-8')
	wiki = WikiCorpus(fname=input_file, lemmatize=False, dictionary={})
	for text in wiki.get_texts():
		out.write(space.join(text) + '\n')
		i += 1
		if (i % 10000 == 0):
			logging.info('Saved {i} articles...'.format(i=i))

	out.close()
	logging.info('Finished saved {i} articles...'.format(i=i))
