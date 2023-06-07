import numpy as np


def calculate(list):
  # list = list with 9 digits
  # if list has <9 elements, return ValueError
  if len(list) != 9:
    raise ValueError('List must contain nine numbers.')

  # convert list into 3x3 numpy array
  arr = np.array(list).reshape((3, 3))

  # get stats for axis0, axis1, flattened array and convert to list
  mean_axis0 = np.mean(arr, axis=0).tolist()
  variance_axis0 = np.var(arr, axis=0).tolist()
  std_axis0 = np.std(arr, axis=0).tolist()
  max_axis0 = np.max(arr, axis=0).tolist()
  min_axis0 = np.min(arr, axis=0).tolist()
  sum_axis0 = np.sum(arr, axis=0).tolist()
  mean_axis1 = np.mean(arr, axis=1).tolist()
  variance_axis1 = np.var(arr, axis=1).tolist()
  std_axis1 = np.std(arr, axis=1).tolist()
  max_axis1 = np.max(arr, axis=1).tolist()
  min_axis1 = np.min(arr, axis=1).tolist()
  sum_axis1 = np.sum(arr, axis=1).tolist()
  mean = np.mean(arr).tolist()
  variance = np.var(arr).tolist()
  std = np.std(arr).tolist()
  max = np.max(arr).tolist()
  min = np.min(arr).tolist()
  sum = np.sum(arr).tolist()

  # return dictionary containing mean, variance, sd, max, min, sum as lists, not numpy array
  calculations = {
    'mean': [mean_axis0, mean_axis1, mean],
    'variance': [variance_axis0, variance_axis1, variance],
    'standard deviation': [std_axis0, std_axis1, std],
    'max': [max_axis0, max_axis1, max],
    'min': [min_axis0, min_axis1, min],
    'sum': [sum_axis0, sum_axis1, sum]
  }

  return calculations
