from re import S
from turtle import distance

class Vertex:
    """
        Class Vertex is to represent the vertex in a graph
        Params: 
            id: the id of the vertex
            connectionTo: the neighbor vertices of the vertex
    """
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.time = -1
        self.finish = -1
        self.pred = None
        self.color = None
        self.distance = 0

    def addNeighbor(self,nbr,weight=0):
        """
            Add neighbor verto with the weight.
        """
        self.connectedTo[nbr] = weight


    def __str__(self):
        return str(self.id)

    def __repr__(self) -> str:
        return str(self.id)


    def getConnections(self):
        """
            Get all connected vertices to this vertex
        """
        return self.connectedTo.keys()

    def getId(self):
        return self.id


    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def getDistance(self):
        return self.distance
    
    def setDiscovery(self, time):
        self.time = time

    def setFinish(self, finish):
        self.finish = finish

    def setPred(self, pred):
        self.pred = pred

    def setColor(self, color):
        self.color = color 

    def getColor(self):
        return self.color

    def getPred(self):
        return self.pred   

    def setDistance(self, distance):
        self.distance = distance