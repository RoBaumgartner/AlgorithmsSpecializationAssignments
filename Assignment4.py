"""Implement the contraction algorithm to find the min-cut in the given undirected graph"""

from random import randint

vertices = []
edges = []

def merge(v1, v2, indexV1, indexV2):
  for vertex in edges[indexV2]:
    print("v1: ", v1, ", v2: ", v2, ", vertex: ", vertex)
    if vertex == v2:
      continue
    vIndex = vertices.index(vertex)
    edges[vIndex].remove(v2) # bidirectional graph, so take out v2 from all vertices it points to
    edges[vIndex].append(v1)
    edges[indexV1].append(vertex)

  vertices.remove(v2)
  del edges[indexV2]

def removeSelfLoops():
  for i in range(len(vertices)):
    while vertices[i] in edges[i]:
      edges[i].remove(vertices[i])

# construct edges
file = open("Assignment4_Input.txt", "r") # Assignment4_Input
for line in file:
  line = line.split()
  vertices.append(int(line[0]))
  edges.append([])
  for num in line[1:]:
    edges[-1].append(int(num))

if __name__ == "__main__":
  n = len(vertices)
  N = n ** 2
  minimum = n

  for iteration in range(N):
    while len(vertices) > 2:
      indexV1 = randint(0, len(vertices) - 1)
      if len(edges[indexV1]) == 0: # TODO
        print(0)
        exit()

      indexV2 = randint(0, len(edges[indexV1]) - 1)
      v1 = vertices[indexV1]
      v2 = edges[indexV1][indexV2]
      if v1 == v2:
        continue

      indexV2 = vertices.index(v2)
      merge(v1, v2, indexV1, indexV2)
      removeSelfLoops()

    removeSelfLoops()
    minimum = min(minimum, len(edges[0]))
    print("Iteration: ", iteration, ", min: ", minimum)

  print("Min-cut: ", minimum)