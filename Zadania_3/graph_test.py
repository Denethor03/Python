from Graph import Graph
import matplotlib.pyplot as plt

if __name__ == "__main__":
    g1 = Graph(5)
    g1.addVertex(0,"A",1,1)
    g1.addVertex(1,"B",1.5,1.5)
    g1.addVertex(2,"C",1.5,0.5)
    g1.addVertex(3,"D",2,0.5)
    g1.addVertex(4,"E",2.5,1.5)
    #g1.addVertex(5,"")
    g1.connectVertexes(0,1,10)
    g1.connectVertexes(0,2,2)
    g1.connectVertexes(1,3,4)
    g1.connectVertexes(1,4,2)
    g1.connectVertexes(3,4,7)
    g1.connectVertexes(2,3,3)
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(min(g1.x_cords)-0.5,max(g1.x_cords)+0.5)
    plt.ylim(min(g1.y_cords)-0.5,max(g1.y_cords)+0.5)

    for u in range(g1.size):
        for v in range(u + 1, g1.size): 
            if g1.edgesWeights[u][v] != 0:
                plt.plot(
                    [g1.x_cords[u], g1.x_cords[v]],
                    [g1.y_cords[u], g1.y_cords[v]],
                    color="lightgray",
                    linewidth=1,
                    zorder=1
                )
                mid_x = (g1.x_cords[u] + g1.x_cords[v]) / 2
                mid_y = (g1.y_cords[u] + g1.y_cords[v]) / 2
                plt.text(mid_x, mid_y, str(g1.edgesWeights[u][v]))

    distances, predacessors = g1.Dijkstra("A")

    path_str = g1.getPath('A', 'E', predacessors)
    print(distances)
    print("Shortest path:", path_str)

    path_nodes = [g1.vertexData.index(v) for v in path_str.split("->") if v]

    for i in range(len(path_nodes) - 1):
        u, v = path_nodes[i], path_nodes[i + 1]
        plt.plot(
            [g1.x_cords[u], g1.x_cords[v]],
            [g1.y_cords[u], g1.y_cords[v]],
            color="red",
            linewidth=3,
            label="Shortest path" if i == 0 else ""
        )

    for i in range(g1.size):
        plt.scatter(g1.x_cords[i], g1.y_cords[i], color="black", s=50, zorder=3)
        plt.text(g1.x_cords[i], g1.y_cords[i] + 0.1, g1.vertexData[i])

    plt.title('Graph with Shortest Path')
    plt.legend()
    #plt.grid(True)
    plt.show()
