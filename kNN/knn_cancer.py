from knn import kNN as my_knn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import time
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt


if __name__ == "__main__":
    
    
    cancer_data = load_breast_cancer()

    data_sizes = [10, 50, 100, 200, 400, 500, len(cancer_data.data)]
    my_times = []
    build_in_times = []

    K = 5
    print(f"Testing with k={K} neighbors")
    for data_size in data_sizes:
        
        X = cancer_data.data[:data_size] # coordinates/features
        y = cancer_data.target[:data_size] # classes
        data = [list(X[i]) + [int(y[i])] for i in range(len(X))]

        train, test = train_test_split(data, test_size=0.2, random_state=42)

        X_train = [x[:-1] for x in train]
        y_train = [x[-1] for x in train]
        X_test = [x[:-1] for x in test]
        y_test = [x[-1] for x in test]
        
        # ====My kNN ====
        my_correct = 0
        
        start = time.time()
        for point , true_class in zip(X_test, y_test):
            my_pred, _ = my_knn(point,train,k = K)
            if my_pred == true_class:
                my_correct += 1
        my_time = time.time() - start
        my_times.append(my_time)
        my_accuracy = my_correct / len(test)
        
        
        #==== Built-in kNN ====
        build_in_correct = 0
        
        start = time.time()

        clf = KNeighborsClassifier(n_neighbors=K)
        clf.fit(X_train, y_train)
        
        build_in_correct = sum(pred == true for pred, true in zip(clf.predict(X_test), y_test))

        build_in_time = time.time() - start 
        build_in_times.append(build_in_time)  
        build_in_accurracy = build_in_correct / len(test)
        
        print(f"Data size: {data_size} | My kNN -> time: {my_time:.4f}s, accuracy: {my_accuracy:.4f} | "
              f"Sklearn kNN -> time: {build_in_time:.4f}s, accuracy: {build_in_accurracy:.4f}")
        
plt.plot(data_sizes, my_times, label="Our kNN", marker='o')
plt.plot(data_sizes, build_in_times, label="Sklearn kNN", marker='o')
plt.xlabel("Data Size")
plt.ylabel("Time (seconds)")
plt.title(f"Performance Comparison of kNN with k={K}")
plt.legend()
plt.grid(True)
plt.show()

