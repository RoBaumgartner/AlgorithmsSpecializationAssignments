"""Implement quicksort with 3 different policies for chosing pivot element. Assumption: input has only distict elements"""

from enum import Enum
from math import floor

class Question(Enum):
  Q1 = 1
  Q2 = 2
  Q3 = 3

# global constant to set question, must be Question()-member
q = Question.Q3

def choosePivot(array, l, r): # 
  if q == Question.Q1:
    return
  elif q == Question.Q2:
    elem = array[l]
    array[l] = array[r]
    array[r] = elem
  else:
    m = floor((l + r) / 2)
    
    values = [array[l], array[m], array[r]]
    indices = [l, m, r]

    iMax = values.index(max(values))
    del values[iMax]
    del indices[iMax]

    iMax = values.index(max(values))
    elem = array[l]
    array[l] = array[indices[iMax]]
    array[indices[iMax]] = elem

def quickSort(array, l, r):
  if l >= r:
    return 0

  choosePivot(array, l, r)
 
  # put pivot in rightous place
  i = l + 1
  for j in range(i, r + 1):
    if array[j] < array[l]:
      elem = array[j]
      array[j] = array[i]
      array[i] = elem
      i += 1
  elem = array[i - 1]
  array[i - 1] = array[l]
  array[l] = elem

  p = i - 1
  nLeft = quickSort(array, l, p - 1)
  nRight = quickSort(array, p + 1, r)

  return nLeft + nRight + len(array[l:r+1]) - 1

if __name__ == "__main__":
  file = open("Assignment3_Input.txt", "r") # Assignment3_Input
  array = [int(i) for i in file]

  n = quickSort(array, 0, len(array) - 1)
  print(n)