import sys
import logging
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

'''
	训练语言模型，将词转化成向量
'''

if __name__ == '__main__':
	program_name = sys.argv[0]
	logger = logging.getLogger(name=program_name)

	logging.basicConfig(format=('%(asctime)s: %(levelname)s: %(message)s'))
	logging.root.setLevel(level=logging.INFO)
	logger.info('running {s}'.format(s=','.join(sys.argv)))

	input_file = sys.argv[1]
	out_model_file = sys.argv[2]
	out_vec_file = sys.argv[3]

	model = Word2Vec(LineSentence(input_file), size=50, window=5, min_count=5, workers=2)
	model.save(out_model_file)
	model.wv.save_word2vec_format(out_vec_file, binary=False)
