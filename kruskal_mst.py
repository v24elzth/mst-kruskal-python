
class Graph: 
  def __init__(self, vertices): 
    self.V = vertices 
    self.graph = [] 

  def addEdge(self, u, v, w): 
    self.graph.append([u, v, w]) 

  def find(self, parent, i): 
    if parent[i] != i: 
      parent[i] = self.find(parent, parent[i]) 
    return parent[i] 

  def union(self, parent, rank, x, y): 
    if rank[x] < rank[y]: 
      parent[x] = y 
    elif rank[x] > rank[y]: 
      parent[y] = x 
    else: 
      parent[y] = x 
      rank[x] += 1

  def KruskalMST(self, pointD): 
    result = [] 
    i, e = 0, 0
    self.graph = sorted(self.graph, key=lambda item: item[2]) 
    parent = [] 
    rank = [] 
    for node in range(self.V): 
      parent.append(node) 
      rank.append(0) 
    while e < self.V - 1: 
      u, v, w = self.graph[i] 
      i = i + 1
      x = self.find(parent, u) 
      y = self.find(parent, v) 
      if x != y: 
        e = e + 1
        result.append([u, v, w]) 
        self.union(parent, rank, x, y) 
    minimumCost = 0
    print("Edges in the constructed MST\n") 
    for u, v, w in result: 
      minimumCost += w 
      orig = pointD[u][0]
      dest = pointD[v][0]
      print(f"{orig:10} -- {dest:10} == {w:8.1f} km")
    print(f"\nMinimum Spanning Tree = {minimumCost:.1f} km")

# main
pointD = {
  0 : ["Monas"],
  1 : ["TMII"],
  2 : ["Ancol"],
  3 : ["PIK"],
  4 : ["Anyer"],
  5 : ["Bogor"],
  6 : ["Safari"],
  7 : ["Kota"],
}

edges = [
  (0, 0, 0),
  (0, 1, 16.04),
  (0, 2, 5.66),
  (0, 3, 11.69),
  (0, 4, 97.7),
  (0, 5, 47.01),
  (0, 6, 63.91),
  (0, 7, 4.7),
  (1, 1, 0),
  (1, 2, 21.05),
  (1, 3, 27.59),
  (1, 4, 107.16),
  (1, 5, 34.38),
  (1, 6, 48.61),
  (1, 7, 20.68),
  (2, 2, 0),
  (2, 3, 8.52),
  (2, 4, 97.83),
  (2, 5, 52.67),
  (2, 6, 69.34),
  (2, 7, 2.19),
  (3, 3, 0),
  (3, 4, 90.01),
  (3, 5, 56.14),
  (3, 6, 74.54),
  (3, 7, 7.52),
  (4, 4, 0),
  (4, 5, 109.68),
  (4, 6, 131.65),
  (4, 7, 96.01),
  (5, 5, 0),
  (5, 6, 22.99),
  (5, 7, 51.41),
  (6, 6, 0),
  (6, 7, 68.59),
]
G = Graph(len(pointD))
for u, v, w in edges:
  G.addEdge(u, v, w)
  

G.KruskalMST(pointD)
