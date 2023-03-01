from queue import Queue
from vertex import Vertex

class Graph:
    """ 
    Class Graph is to manage and represent a graph by managing the list of vertices.
    Params:
        vertList: the list of vertics
        numVertices: the number of vertices
    """
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        """
            Add vertex with key
        """
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        """
            Get vertex
        """
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None


    def __contains__(self,n):
        return n in self.vertList


    def addEdge(self,s,d,weight=0):
        """
            Add edge by adding a start vertex and a destination vertex
            s: a start vertex
            d: a destinaton vertex
        """
        if s not in self.vertList:
            nv = self.addVertex(s)
        if d not in self.vertList:
            nv = self.addVertex(d)
        self.vertList[s].addNeighbor(self.vertList[d], weight)

    def getVertices(self):
        """
            Get list of vertices
        """
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


    
class DFSGraph(Graph):
    """ 
        Class DFSGraph derive from class Graph
        DFSGraph provide method to suport for traverse all vertices of the graph using Deep Frist Search algorithm
    """
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        """
            Traverse all vertices using DFS algorithm. the vertex will remember the neighbor vertex go to it.
            After that we can get the route to any vertex quickly
        """
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(None)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        self.time += 1
        startVertex.setFinish(self.time)

    def traverse(self, y):
        """
            Print the route to any vertex.
        """
        x = y
        trace = []
        while (x.getPred()):
            trace.append(x)
            x = x.getPred()
            if(x.getPred() == None):
                trace.append(x)

        trace = reversed(trace)
        result = "->".join(str(v.getId()) for v in trace)
        print(result)



class BFSGraph(Graph):
    """ 
        Class BFSGraph derive from class Graph
        BFSGraph provide method to suport for traverse all vertices of the graph using Breadth Frist Search algorithm
    """
    def __init__(self):
        super().__init__()
        self.time = 0

    def bfs(self):
        """
            Traverse all vertices using BFS algorithm. the vertex will remember the neighbor vertex go to it.
            After that we can get the route to any vertex quickly
        """
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(None)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.bfsVisit(aVertex)

    def bfsVisit(self, start):
        start.setDistance(0)
        start.setPred(None)
        vertQueue = Queue()
        vertQueue.put(start)
        while (vertQueue.qsize() > 0):
            currentVert = vertQueue.get()
            for nbr in currentVert.getConnections():
                if (nbr.getColor() == 'white'):
                    nbr.setColor('gray')
                    nbr.setDistance(currentVert.getDistance() + 1)
                    nbr.setPred(currentVert)
                    vertQueue.put(nbr)
            currentVert.setColor('black')

    def traverse(self, y):
        """
            Print the route to any vertex.
        """
        x = y
        trace = []
        while (x.getPred()):
            trace.append(x)
            x = x.getPred()
            if(x.getPred() == None):
                trace.append(x)

        trace = reversed(trace)
        result = "->".join(str(v.getId()) for v in trace)
        print(result)

