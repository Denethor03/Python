class Graph:
    def __init__(self,size):
        self.size = size
        self.vertexData = ['']*size
        self.edgesWeights = [[0]*size for _ in range(size)]
        
    def addVertex(self,index,data):
        if index < self.size:
            self.vertexData[index] = data

    def connectVertexes(self,u,v,weight):
        if u < self.size and v < self.size:
            self.edgesWeights[u][v] = weight
            self.edgesWeights[v][u] = weight

    def Dijkstra(self,startingVertex):
        distances = [float('inf')]*self.size
        startingVertexIndex = self.vertexData.index(startingVertex)
        visited = [False] * self.size
        distances[startingVertexIndex] = 0
        previousNodes = [None] * self.size

        for _ in range(self.size):
            minDist = float("inf")
            closestIndex = None
            for i in range(self.size):
                if not visited[i] and distances[i] < minDist:
                    closestIndex = i
                    minDist = distances[i]
            

            if closestIndex == None:
                break
            
            visited[closestIndex] = True

            for v in range(self.size):
                if self.edgesWeights[closestIndex][v] != 0 and not visited[v]:
                    distSum = distances[closestIndex] + self.edgesWeights[closestIndex][v]
                    if distSum < distances[v]:
                        distances[v] = distSum
                        previousNodes[v] = closestIndex
        return distances, previousNodes
    
    def getPath(self,start,end,previousNodes):
        path = ""
        currentVertex = self.vertexData.index(end)
        while currentVertex != None:
            path = "->" + self.vertexData[currentVertex] + path
            currentVertex = previousNodes[currentVertex]
            if currentVertex == self.vertexData.index(start):
                path = self.vertexData[currentVertex] + path
                break
        return path


if __name__ == "__main__":
    g1 = Graph(5)
    g1.addVertex(0,"A")
    g1.addVertex(1,"B")
    g1.addVertex(2,"C")
    g1.addVertex(3,"D")
    g1.addVertex(4,"E")
    g1.connectVertexes(0,1,5)
    g1.connectVertexes(0,2,2)
    g1.connectVertexes(1,3,4)
    g1.connectVertexes(1,4,1)
    g1.connectVertexes(3,4,7)
    g1.connectVertexes(2,3,3)
    distances, predacessors = g1.Dijkstra("A")
    print(distances)
    print(g1.getPath('A','E',predacessors))