import sys
import gensim

'''
	模型匹配检验
'''

if __name__ == '__main__':
	model_file = sys.argv[1]
	model = gensim.models.Word2Vec.load(model_file)
	# gensim.models.keyedvectors.

	word = model.most_similar('VIPKID')
	for t in word:
		print('{0} {1}'.format(t[0], t[1]))
