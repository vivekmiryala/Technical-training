from collections import defaultdict

class Graph:
  def __init__(self, vertices):
    self.V = vertices
    self.edges = []

  def add_edge(self, u, v, weight):
    self.edges.append((weight, u, v))

  def find(self, parent, i):
    if parent[i] == i:
      return i
    return self.find(parent, parent[i])

  def union(self, parent, rank, x, y):
    x_root = self.find(parent, x)
    y_root = self.find(parent, y)

    # Attach the smaller rank tree under the root of the higher rank tree
    if rank[x_root] < rank[y_root]:
      parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
      parent[y_root] = x_root
    # When ranks are same, make root of x as root of y and increment its rank.
    else:
      parent[y_root] = x_root
      rank[x_root] += 1

  # Function to construct MST using Kruskal's Algorithm
  def kruskal_mst(self):
    result = []  # This will store the constructed MST
    parent = [None] * self.V
    rank = [0] * self.V

    # Sort edges in non-decreasing order of their weight
    self.edges.sort(key=lambda item: item[0])

    # Allocate memory for parent
    for node in range(self.V):
      parent[node] = node

    i = 0 
    count = 0 

    while count < self.V - 1:
      weight, u, v = self.edges[i]
      i += 1
      x = self.find(parent, u)
      y = self.find(parent, v)

      if x != y:
        result.append((weight, u, v))
        self.union(parent, rank, x, y)
        count += 1

    # Check if all nodes belong to the same connected component
    if self.find(parent, 0) != self.find(parent, self.V - 1):
      print("Graph doesn't have a Really Special SubTree")
      return

    print("Following are the edges in the constructed MST")
    for edge in result:
      print("%d -- %d == %d" % (edge[1], edge[2], edge[0]))



vertices = 5
graph = Graph(vertices)

graph.add_edge(0, 1, 2)
graph.add_edge(0, 3, 1)
graph.add_edge(1, 2, 4)
graph.add_edge(3, 4, 3)
graph.add_edge(3, 2, 1)
graph.add_edge(4, 2, 2)
graph.add_edge(3, 0, 5)

graph.kruskal_mst()
