# approach 1 

def interchange_(L):
    first_ = L[0]
    L[0] = L[-1]
    L[-1] = first_ 
    return L

print(interchange_([1,2,3,4,5,6]))  # [6, 2, 3, 4, 5, 1]


# approach 2 

def swapList(newList):
    
    newList[0], newList[-1] = newList[-1], newList[0]

    return newList
    
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))


# approach 3

def swapList(list):
    
    start, *middle, end = list
    list = [end, *middle, start]
    
    return list #(list, end, *middle, start)
    
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))   # [24, 35, 9, 56, 12]



# approach 4 


# Swap function
def swapList(list):
    
    first = list.pop(0)   
    last = list.pop(-1)
    
    list.insert(0, last)  
    list.append(first)   
    
    return list
    
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))

