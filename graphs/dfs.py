#from collections import defaultdict

class Vertex:
    
    def __init__(self, name):
        self.name = name
        self.color = "white"
        self.parent = None
        self.d = 0
        self.f = 0

    def __repr__(self):
        return f"{self.name}"


class Graph:

    def __init__(self):
        
        self.adj = {}
        self.time = 0
        self.vertices = {}

    def addVertex(self, name):
        if name not in self.vertices:
            self.vertices[name] = Vertex(name)
            self.adj[self.vertices[name]] = []

    def addEdge(self, u, v):
        self.addVertex(u)
        self.addVertex(v)
        u = self.vertices[u]
        v = self.vertices[v]
        self.adj[u].append(v)

    def dfs(self):
        for u in self.vertices.values():
            u.color = "white"
            u.parent = None
        
        self.time = 0
        for u in self.vertices.values():
            if u.color == "white":
                self.dfsVisit(u)

    def dfsVisit(self, u):
        self.time += 1
        u.d = self.time
        u.color = "grey"
        for v in self.adj[u]:
            if v.color == "white":
                v.parent = u
                self.dfsVisit(v)
            
            u.color = "black"
            self.time += 1
            u.f = self.time
    
    def printDFS(self):
        for v in self.vertices.values():
            print(f"{v.name}: d={v.d}, f={v.f}, parent={v.parent.name if v.parent else None}")


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,2)
    g.addEdge(2,0)
    g.addEdge(2,3)
    g.addEdge(3,3)

    g.dfs()
    g.printDFS()