class Graph:
    def __init__(self,size):
        self.size = size
        self.x_cords = [None] * self.size
        self.y_cords = [None] * self.size
        self.vertexData = ['']*size
        self.edgesWeights = [[0]*size for _ in range(size)]

        
    def addVertex(self,index,data,x,y):
        if index < self.size:
            self.vertexData[index] = data
            self.x_cords[index] = x
            self.y_cords[index] = y

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


