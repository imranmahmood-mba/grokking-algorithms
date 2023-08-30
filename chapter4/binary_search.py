def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)
    else:
        return -1  # Target not found

def binary_search_non_recursive(arr, target):
    low = 0
    max = len(arr) - 1
    while low <= max:
        mid = (max + low) // 2
        if target > arr[mid]:
            low = mid + 1
        elif target < arr[mid]:
            max = mid - 1
        else:
            return mid
    return -1

