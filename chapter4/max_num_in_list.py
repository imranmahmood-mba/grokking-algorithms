# non recursive solution
def max_num_in_list(arr):
    max = 0
    for num in arr:
        if num > max:
            max = num
    return max
        
def max_num_in_list_recurive(arr):
    if arr == []:
        return arr
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max_num_in_list_recurive(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

# came up with the non-recursive solution, tried to do the recursive
# solution myself but struggled, used answer from books