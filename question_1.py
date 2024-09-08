def findTwoUniqueNumbers(arr):
    res = 0
    
    for num in arr:
        res ^= num

    set_bit = res & -res
    
   
    x = y = 0
    
    for num in arr:
        if num & set_bit:
            x ^= num 
        else:
            y ^= num 
    
    return sorted([x, y])

arr1 = eval(input())
print(findTwoUniqueNumbers(arr1)) 

