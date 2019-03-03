from knn_algorithm import euclidean_distance, get_neighbors, get_response, get_accuracy
import codecs

def test_instance():
	data1 = [2, 2, 2, 'a']
	data2 = [4, 4, 4, 'b']
	distance = euclidean_distance(data1, data2, 3)
	print('distance: {d}'.format(d=distance))


def test_neighbors():
	train_set = [[2, 2, 2, 'a'], [4, 4, 4, 'b']]
	test_instance = [5, 5, 5]
	k = 1
	neighbors = get_neighbors(training_set=train_set,
	                          test_instance=test_instance, k=k)
	print('neighbors: {n}'.format(n=neighbors))


def test_response():
	neighbors = [[1, 1, 1, 'a'], [2, 2, 2, 'b'], [3, 3 ,3, 'c']]
	response = get_response(neighbors=neighbors)
	print('response: {r}'.format(r=response))


def test_accuracy():
	test_set = [[1, 1, 1, 'a'], [2, 2, 2, 'a'], [3, 3 ,3, 'c']]
	predictions = ['a', 'a', 'a']
	accuracy = get_accuracy(test_set=test_set, predictions=predictions)
	print('accuracy: {a}'.format(a=accuracy))


def build_vecs(file_path):
    file_vecs = []
    with codecs.open(file_path, 'r', encoding='utf-8') as contents:
        for line in contents:
            line = line.strip()
            line_array = line.split('\t')
            type_value = line_array[0]
            sentence = line_array[1]
            print('{0}, {1}'.format(type_value, sentence))


if __name__ == '__main__':
	# test_neighbors()
	# test_response()
	# test_accuracy()
	build_vecs('D:\\lijiangming\\docs\\algorithm\\library\\sentence\\sentence.txt')