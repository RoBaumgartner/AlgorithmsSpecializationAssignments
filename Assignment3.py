"""Implement quicksort with 3 different policies for chosing pivot element. Assumption: input has only distict elements"""

from enum import Enum

class Question(Enum):
  Q1 = 1
  Q2 = 2
  Q3 = 3

# global constant to set question, must be Question()-member
q = Question.Q2

def choosePivot(array, l, r): # 
  if q == Question.Q1:
    return l
  elif q == Question.Q2:
    return r
  else:
    pass

def quickSort(array, l, r, n):
  if l >= r:
    return 0

  p = choosePivot(array, l, r)
 
  # put p in rightous place
  i = l
  for j in range(i, r + 1):
    if i == p:
      i += 1
    if array[j] < array[p]: # swap i and j
      elem = array[j]
      array[j] = array[i]
      array[i] = elem
      i += 1
  elem = array[i - 1]
  array[i - 1] = array[p]
  array[p] = elem

  p = i - 1
  n += quickSort(array, l, p - 1, n)
  n += quickSort(array, p + 1, r, n)

  return n + 1

if __name__ == "__main__":
  file = open("Test1.txt", "r") # Assignment3_Input
  array = [int(i) for i in file]

  n = quickSort(array, 0, len(array) - 1, 0)
  print(array)