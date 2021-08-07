def binary_search(input_array, value):
    first = 0
    last = len(input_array)-1
    while last >= first:
        midpoint = (first+last)//2
        if input_array[midpoint] == value:
            return midpoint
        elif value > input_array[midpoint]:
            first = midpoint+1
        else:
            last = midpoint-1
            
    return -1
