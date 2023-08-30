# Write out a recursive function to count the numbere of items in a list

def total_count(arr):
    if len(arr) == 0: # base case
        return 0 
    return 1 + total_count(arr[1:]) # recursive case

# Got this correct. Followed the recursive_sum answer to get a general idea.
# Originally tried to sum the length of the array and the 
# recursive call but realized that I had to sum 1 & the recursive 
# call