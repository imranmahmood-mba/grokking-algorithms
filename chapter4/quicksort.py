# my approach
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = len(arr) // 2
        greater = [i for i in arr if i > arr[pivot]]
        equal = [i for i in arr if i == arr[pivot]]
        less = [i for i in arr if i < arr[pivot]]
        return quicksort(less) + equal + quicksort(greater)

# my approach to fit my solution to the book's 
def quicksort_edit(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        greater = [i for i in arr[1:] if i > pivot]
        less = [i for i in arr[1:] if i <= pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
# the book's approach
def quicksort_book(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
arr = [18, 1,1,1, 2, 3, 8, 4, 4, 3 ]

print(quicksort(arr))