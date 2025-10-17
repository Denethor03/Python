from multiprocessing import Pool
import math

def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[-1]
    left = [x for x in array if x < pivot]
    mid = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quicksort(left) + mid + quicksort(right)

def merge_sorted_lists(lists):
    result = []
    indices = [0]*len(lists) # this keeps track of indexes of individual lists
    while True:
        smallest = None
        smallest_ind = -1
        for i,lst in enumerate(lists):
            if indices[i] < len(lst): # if array is "finished" skip
                val = lst[indices[i]]
                if smallest == None or val < smallest:
                    smallest = val
                    smallest_ind = i
        if smallest_ind == -1:
            break
        result.append(smallest)
        indices[smallest_ind]+=1
    return result 

def parallel_sort(data, n_processes=4):
    if len(data) == 0:
        return []

    chunk_size = math.ceil(len(data) / n_processes)
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    with Pool(n_processes) as pool:
        sorted_chunks = pool.map(quicksort, chunks) #returns list of lists

    return merge_sorted_lists(sorted_chunks)

if __name__ == "__main__":
    import random
    arr = [random.randint(0, 100) for _ in range(30)]
    print("Unsorted:", arr)
    sorted_arr = parallel_sort(arr)
    print("Sorted:", sorted_arr)