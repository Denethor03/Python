import matplotlib.pylab as plt
import numpy as np
import random

def kNN(point,data,k):
    
    dataDist = [d + [distance(point,d)] for d in data]

    dataDist.sort(key = lambda x : x[-1])
    
    classes = [x[-2] for x in dataDist[:k]]

    return max(set(classes), key = classes.count), dataDist[k-1][-1]
        

def distance(p1,p2):
    return sum((a-b)**2 for a,b in zip(p1,p2))**0.5 # zip returns pairs of elements

def generate_data(n_per_class=50):
    data = []
    for _ in range(n_per_class):
        x = random.uniform(1, 3)
        y = random.uniform(0, 2)
        data.append([x, y, 'A'])
    for _ in range(n_per_class):
        x = random.uniform(3, 5)
        y = random.uniform(3, 5)
        data.append([x, y, 'B'])
    for _ in range(n_per_class):
        x = random.uniform(1, 2)
        y = random.uniform(2, 5)
        data.append([x, y, 'C'])
    return data


if __name__ == "__main__":
    
    data = generate_data()
    classes = set(c[2] for c in data) # set removes duplicates

    for c in classes:
        X = [x[0] for x in data if x[2]==c]
        Y = [x[1] for x in data if x[2]==c]
        plt.scatter(X,Y, label = c)
    
    myPoint = [2.5,2.5]
    cls, rad = kNN(myPoint,data,4)
    plt.scatter(myPoint[0],myPoint[1],marker = 'x')
    circle = plt.Circle(myPoint,rad,fill = False)
    plt.text(myPoint[0],myPoint[1]+0.1,cls)
    plt.gca().add_patch(circle)
    plt.gca().set_aspect(1.0)
    plt.legend()
    plt.xlim([0,5])
    plt.ylim([0,5])
    plt.show()
    
    