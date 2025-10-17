from pararell_sort import parallel_sort
import time
import random
import matplotlib.pyplot as plt


if __name__ == "__main__":
    data_sizes = [100,10000,50000,500000,1000000]
    process_count = [2, 4, 8]
    results = {}
    
    for p in process_count:
        times = []
        
        for d in data_sizes:
            random_array = [random.randint(0,d) for _ in range(0,d)]
            start = time.time()
            parallel_sort(random_array,p)
            stop = time.time()
            times.append(stop-start)

        results[p] = times

    for p,times in results.items():
        plt.plot(data_sizes, times, marker='o', label=f'{p} processes')
    
    plt.xlabel('Data size')
    plt.ylabel('Execution time in s')
    plt.title('Pararlael performance graph or smth')
    plt.legend()
    plt.grid(True)
    plt.show()


            