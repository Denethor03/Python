import timeit
import numpy as np
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier
from memory_profiler import memory_usage
import string
from knn import kNN as my_knn
from matplotlib import pyplot as plt



def sklearn_kNN(point, X_train, y_train, k):  
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    point_reshaped = np.array(point).reshape(1, -1)
    return knn.predict(point_reshaped)[0]


def run_benchmark(): 
    data_sizes = [100, 500, 1000, 2500, 5000, 10000]
    k_neighbors = 5
    results = []
    n_classes = 3 

    print("kNN \"benchmark\"")
    print("-" * 40)
    i = 0
    for size in data_sizes:
        print(f"Testing with data size: {size}") 
        X, y_numeric = make_classification(
            n_samples=size,
            n_features=2,
            n_informative=2,
            n_redundant=0,
            n_classes=n_classes,
            n_clusters_per_class=1,
            random_state=42
        )

        if i==0:
            plt.scatter(X[:, 0], X[:, 1], c=y_numeric)
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("Data")
            plt.show()
            i+=1

        label_map = {i: char for i, char in enumerate(string.ascii_uppercase)}
        y_char = [label_map[label] for label in y_numeric]
        
        my_data_format = [
            [X[i, 0], X[i, 1], y_char[i]] for i in range(size)
        ]
        
        test_point = [0.5, 0.5]

        
        my_time = timeit.timeit(
            lambda: my_knn(test_point, my_data_format, k_neighbors),
            number=10
        )
        sklearn_time = timeit.timeit(
            lambda: sklearn_kNN(test_point, X, y_char, k_neighbors),
            number=10
        )

        
        my_mem = max(memory_usage(
            (my_knn, (test_point, my_data_format, k_neighbors))
        ))
        sklearn_mem = max(memory_usage(
            (sklearn_kNN, (test_point, X, y_char, k_neighbors))
        ))
        
        results.append({
            "size": size,
            "my_time_avg": my_time / 10,
            "sklearn_time_avg": sklearn_time / 10,
            "my_mem_peak": my_mem,
            "sklearn_mem_peak": sklearn_mem,
        })

 
    print("\n" + "="*70)
    print("Benchmark Results")
    print("="*70)
    print(f"{'Data Size':<12} | {'My kNN Time (s)':<20} | {'Sklearn kNN Time (s)':<22} | {'My kNN Mem (MiB)':<20} | {'Sklearn kNN Mem (MiB)':<22}")
    print("-" * 105)

    for res in results:
        print(
            f"{res['size']:<12} | "
            f"{res['my_time_avg']:<20.6f} | "
            f"{res['sklearn_time_avg']:<22.6f} | "
            f"{res['my_mem_peak']:<20.2f} | "
            f"{res['sklearn_mem_peak']:<22.2f}"
        )


if __name__ == '__main__':
    run_benchmark()