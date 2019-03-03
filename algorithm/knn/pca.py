import sys


import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from numpy import mat, mean, cov, linalg, argsort, shape, nonzero, isnan


def load_data(csv_file):
    data = pd.read_csv(csv_file)
    # x = data[list(range(401))]

    print('data: {x}'.format(x=data))

    return mat(data)


def pca(data_mat, max_feature=105):
    mean_value = mean(data_mat, axis=0)

    data_rem_mat = data_mat - mean_value
    cov_mat = cov(data_rem_mat, rowvar=0)
    print('cov mat: {cm}'.format(cm=cov_mat))

    feature_value, feature_vect = linalg.eig(mat(cov_mat))
    print('feature_value: {fv}'.format(fv=feature_value))
    print('feature_vect: {fv}'.format(fv=feature_vect))

    fea_value_sort = argsort(feature_value)
    fea_value_topN = fea_value_sort[: -(max_feature + 1): -1]
    red_eig_vects = feature_vect[:, fea_value_topN]
    print('topN: {t}'.format(t=red_eig_vects))
    print(shape(red_eig_vects))

    low_data_mat = data_rem_mat * red_eig_vects
    reco_mat = low_data_mat * red_eig_vects.T + mean_value
    print('low_data_mat: {ldm}'.format(ldm=low_data_mat))

    return low_data_mat, reco_mat


def plot_w(low_data_mat, reco_mat):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(low_data_mat[:, 0], low_data_mat[:, 1], marker='*', s=90)
    ax.scatter(reco_mat[:, 0], reco_mat[:, 1], marker='*', s=50, c='red')
    plt.show()


def replace_nan_with_mean(file_path):
    dat_mat = load_data(csv_file=file_path)
    num_feat = shape(dat_mat)[1]
    for i in range(num_feat):
        mean_value = mean(dat_mat[nonzero(~isnan(dat_mat[:, i].A))[0], i])
        # set NaN values to mean
        dat_mat[nonzero(isnan(dat_mat[:, i].A))[0], i] = mean_value

    print('dat_mat: {dm}'.format(dm=dat_mat))

    return dat_mat


def test():
    csv_file = sys.argv[1]
    df = pd.read_csv(csv_file)
    data = df.iloc[:, :401]
    # type_array = df.iloc[:, 401]

    n_components = 400
    pca = PCA(n_components=n_components)
    pca.fit(data)

    plt.figure(1, figsize=(4, 3))
    plt.clf()
    plt.axes([.2, .2, .7, .7])
    plt.plot(pca.explained_variance_, linewidth=2)
    plt.axis('tight')
    plt.xlabel('n_components')
    plt.ylabel('explained_variance_')
    plt.show()


if __name__ == '__main__':
    file_path = sys.argv[1]
    data_mat = replace_nan_with_mean(file_path=file_path)
    low_data_mat, reco_mat = pca(data_mat=data_mat, max_feature=2)
    plot_w(low_data_mat=low_data_mat, reco_mat=reco_mat)
