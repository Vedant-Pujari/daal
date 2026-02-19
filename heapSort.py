def heapify(arr,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left<n and arr[left]>arr[largest]:
        largest = left

    if right<n and arr[right]>arr[largest]:
        largest = right

    if largest!=i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)

def heap_sort(arr,n=None):
    if n is None:
        n=len(arr)

        for i in range(n//2-1,-1,-1):
            heapify(arr,n,i)

    if n<=1:
        return 
    arr[0],arr[n-1] = arr[n-1],arr[0]

    heap_sort(arr,n-1)

arr = [12,11,13,5,6,7]
print("Original array: ")
print(arr)
heap_sort(arr)
print("Sorted array: ")
print(arr)