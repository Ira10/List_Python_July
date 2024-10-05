######  Python Program to Find Largest Number in a List

######  5th Oct

######## 1. Ascending

list1 = [10, 20, 4, 45, 99]

list1.sort()

print("Largest element is:", list1[-1])    # Largest element is: 99

#########   2. Max method

list1 = [10, 20, 4, 45, 99]

print("Largest element is:", max(list1))    # Largest element is: 99


#############  3.  Without 'built-in' function

def myMax(list1):
    max = list1[0]
    for x in list1:
        if x > max:
            max = x
    return max

# Driver code
list1 = [10, 20, 4, 45, 99]
print("Largest element is:", myMax(list1))  # Largest element is: 99



#########   4. Lambda function

lst = [20, 10, 20, 4, 100]
print(max(lst, key=lambda value: int(value)) )   #### 100


########    5. Reduce func

from functools import reduce
lst = [20, 10, 20, 4, 100]
largest_elem = reduce(max, lst)
print(largest_elem)    ## 100




