import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from collections import Counter
import keras

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


def kNN_vectorized(query_point, X_data, y_data, k):
    distances = np.linalg.norm(X_data - query_point, axis=1)

    nearest_indices = np.argsort(distances)[:k]

    nearest_labels = y_data[nearest_indices]

    most_common = Counter(nearest_labels).most_common(1)

    return most_common[0][0]


if __name__ == "__main__":

    (x_train_full, y_train_full), (x_test_full, y_test_full) = keras.datasets.mnist.load_data()

    X_all = np.concatenate((x_train_full, x_test_full))
    y_all = np.concatenate((y_train_full, y_test_full))
    X_all = X_all.reshape(len(X_all), -1).astype('float32') / 255.0

    # PCA HERE
    pca = PCA(n_components=50)
    X_all_pca = pca.fit_transform(X_all)

    data_sizes = list(range(1000, len(X_all), 10000))

    times_vectorized = []
    times_sklearn = []

    K = 3
    last_y_test = None
    last_y_pred_sklearn = None

    print(f"\nTesting with k={K} neighbors on MNIST (PCA reduced)...")
    print("-" * 90)
    print(f"{'Size':<6} {'Numpy Time':<10} {'Numpy Acc':<10} | {'Sklearn Time':<10}")
    print("-" * 90)

    for size in data_sizes:

        X_subset = X_all_pca[:size]
        y_subset = y_all[:size]

        X_train, X_test, y_train, y_test = train_test_split(X_subset, y_subset, test_size=0.2, random_state=42)

        # optimized
        start = time.time()
        vect_correct = 0
        for i in range(len(X_test)):
            pred = kNN_vectorized(X_test[i], X_train, y_train, k=K)
            if pred == y_test[i]:
                vect_correct += 1

        time_vect = time.time() - start
        acc_vect = vect_correct / len(y_test)
        times_vectorized.append(time_vect)
        # ======================

        # build in KNN from sklearn
        start = time.time()
        clf = KNeighborsClassifier(n_neighbors=K)
        clf.fit(X_train, y_train)

        preds = clf.predict(X_test)
        sklearn_correct = np.sum(preds == y_test)

        time_sklearn = time.time() - start
        acc_sklearn = sklearn_correct / len(y_test)
        times_sklearn.append(time_sklearn)

        if size == data_sizes[-1]:
            last_y_test = y_test
            last_y_pred_sklearn = preds
        # ========================

        print(f"{size:<6} | {time_vect:<10.4f} {acc_vect:<10.4f} | {time_sklearn:<10.4f}")


    plt.figure(figsize=(10, 6))
    plt.plot(data_sizes, times_vectorized, label="Optimized kNN (NumPy)", marker='s')
    plt.plot(data_sizes, times_sklearn, label="Sklearn Built-in", marker='^')
    plt.xlabel("Dataset Size (Number of Images)")
    plt.ylabel("Time (seconds)")
    plt.title(f"kNN Performance: NumPy vs Sklearn on MNIST (PCA 784->50)")
    plt.legend()
    plt.grid(True)
    plt.show()

    if last_y_test is not None:
        cm_sklearn = confusion_matrix(last_y_test, last_y_pred_sklearn)


        display_labels = np.arange(10)

        disp_sklearn = ConfusionMatrixDisplay(confusion_matrix=cm_sklearn,
                                              display_labels=display_labels)

        plt.figure(figsize=(10, 8))
        disp_sklearn.plot(cmap=plt.cm.cividis, ax=plt.gca())
        plt.title(f"Confusion Matrix - Sklearn kNN on MNIST (k={K}, PCA 50D)")
        plt.show()