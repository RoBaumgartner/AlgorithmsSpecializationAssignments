# Task: Count inversions
import numpy as np

def returnArray():
  file = open("Assignment2_Input.txt", "r")
  arr = []
  for line in file:
    arr.append(int(line))
  
  return np.array(arr)

def countSplitInversions(A, B):
  counter, indexLeft, indexRight = 0, 0, 0
  sortedArray = []

  while indexLeft < len(A):
    if A[indexLeft] < B[indexRight]:
      sortedArray.append(A[indexLeft])
      indexLeft += 1
      if indexLeft == len(A):
        sortedArray.extend(B[indexRight:])
        break
    elif A[indexLeft] > B[indexRight]:
      sortedArray.append(B[indexRight])
      counter += (len(A) - indexLeft)
      indexRight += 1
      if indexRight == len(B):
        sortedArray.extend(A[indexLeft:])
        break

  return sortedArray, counter

def sortAndCount(array):
  n = len(array)
  if n == 1:
    return array, 0

  A, x = sortAndCount(array[:n/2])
  B, y = sortAndCount(array[n/2:])
  C, z = countSplitInversions(A, B)

  return C, x + y + z

if __name__ == "__main__":

  array = returnArray()
  _, n = sortAndCount(array)
  print(n)