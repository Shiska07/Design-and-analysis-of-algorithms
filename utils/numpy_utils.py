import numpy as np


def calculate_2d_mean_median_variance_columnwise(x):
    arr = np.array(x)
    r, c = arr.shape

    sum = np.zeros((1, c))
    for i in range(r):
        sum = sum + arr[i, :]
    mean = sum/r

    if r % 2:
        mid1 = r//2
        mid2 = mid1 + 1
        median = (arr[mid1, :] + arr[mid2, :]) / 2
    else:
        mid = r//2 + 1
        median = arr[mid, :]

    var = np.zeros((1, c))
    for i in range(r):
        var = var + np.square(arr[i, :] - mean)
    var = var/(r-1)

    return mean.tolist(), median.tolist(), np.transpose(var).tolist()


def calculate_2d_mean_median_variance_rowwise(x):
    arr = np.array(x)
    r, c = arr.shape

    sum = np.zeros(r)
    sum = np.transpose(sum)
    for i in range(c):
        sum = sum + arr[:, i]
    mean = sum/c
    print(mean)

    if c % 2:
        mid1 = c//2
        mid2 = mid1 + 1
        median = (arr[:, mid1] + arr[:, mid2]) / 2
    else:
        mid = c//2 + 1
        median = arr[:, mid]
    print(median)

    var = np.zeros(r)
    var = np.transpose(var)
    for i in range(c):
        var = var + np.square(arr[:, i] - mean)
    var = var/(c-1)

    return mean.tolist(), median.tolist(), np.transpose(var).tolist()
