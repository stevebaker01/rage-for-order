import random


def binary_matrix(x, y):
    mat = []
    bins = ('1', '0', '0')
    for i in range(x):
        row = ''
        for j in range(y):
            row += bins[random.randint(0, 2)]
        mat.append(row)
    return mat
