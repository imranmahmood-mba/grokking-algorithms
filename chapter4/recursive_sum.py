# Converting this code:
#  def sum(arr):
    # total = 0 
    # for x in arr:
    #     total += x
    # return total

def sum(arr):
    if arr == []: # base case
        return 0
    return arr[0] + sum(arr[1:]) # recursive case


# Struggled with this, had to look at the answer

    