from collections import defaultdict


class Graph:

    def __init__(self):
        #storing graph in a dictionary
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    
