from numpy import random

def bubblesort(array):
    for i in range(0,len(array)-1):
        for j in range(0,len(array)-1-i):
            if(array[j]>array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
    

def partition(array,low,high):
    i = low - 1
    pivot = array[high]
    for j in range(low,high):
        if(array[j]<pivot):
            i+=1
            array[i], array[j] = array[j], array[i]
    
    array[i+1], array[high] = array[high], array[i+1]
    
    return i+1

def quicksort(array,low, high):
    if low < high:
        pivot = partition(array,low,high)

        quicksort(array,low,pivot-1)
        quicksort(array,pivot+1,high)

if __name__ == "__main__":
    random_array = random.randint(1,50,size=10)
    #print(f"Unsorted:   {random_array}")
    #bubblesort(random_array)
    print(f"Bubblesort: {random_array}")
    quicksort(random_array,0,len(random_array)-1)
    print(f"Quicksort: {random_array}")
    
    