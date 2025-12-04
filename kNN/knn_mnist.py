from knn import kNN as my_knn
from keras.datasets import mnist
from sklearn.model_selection import train_test_split
import time
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt
import numpy as np

if __name__ == "__main__":
    
    
    (X_train_full, y_train_full), (X_test_full, y_test_full) = mnist.load_data()

   
    X_all = np.vstack((X_train_full, X_test_full))
    y_all = np.hstack((y_train_full, y_test_full))

    
    X_all = X_all.reshape(len(X_all), 784).astype(np.float32)

    
    X_all /= 255.0

    
    data_sizes = list(range(1000, len(X_all), 5000))
    my_times = []
    build_in_times = []

    K = 5
    print(f"Testing with k={K} neighbors")

    for data_size in data_sizes:
        
        X = X_all[:data_size]
        y = y_all[:data_size]

        
        data = [list(X[i]) + [int(y[i])] for i in range(len(X))]

        train, test = train_test_split(data, test_size=0.2, random_state=42)

        X_train = [x[:-1] for x in train]
        y_train = [x[-1] for x in train]
        X_test = [x[:-1] for x in test]
        y_test = [x[-1] for x in test]

        # ==== My kNN ====
        '''my_correct = 0
        start = time.time()

        for point, true_class in zip(X_test, y_test):
            my_pred, _ = my_knn(point, train, k=K)
            if my_pred == true_class:
                my_correct += 1

        my_time = time.time() - start
        my_times.append(my_time)
        my_accuracy = my_correct / len(test)
        '''
        # ==== Built-in kNN ====
        start = time.time()
        clf = KNeighborsClassifier(n_neighbors=K)
        clf.fit(X_train, y_train)

        sklearn_correct = sum(pred == t for pred, t in zip(clf.predict(X_test), y_test))

        build_in_time = time.time() - start
        build_in_times.append(build_in_time)
        sklearn_accuracy = sklearn_correct / len(test)

        print(f"Data size: {data_size}  | "
              f"Sklearn kNN -> time: {build_in_time:.4f}s, accuracy: {sklearn_accuracy:.4f}")

#plt.plot(data_sizes, my_times, label="My kNN", marker='o')
plt.plot(data_sizes, build_in_times, label="Sklearn kNN", marker='o')
plt.xlabel("Data Size")
plt.ylabel("Time (seconds)")
plt.title(f"Performance Comparison of kNN with k={K} (MNIST)")
plt.legend()
plt.grid(True)
plt.show()