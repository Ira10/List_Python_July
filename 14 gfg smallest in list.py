#############     Python program to find smallest number in a list  

#####    4th Oct


######  1. Ascending Order  with sort

list1 = [10, 20, 4, 45, 99]

list1.sort()

# printing the first element
print("Smallest element is:", list1[0])    # Smallest element is: 4


######  1. Descending Order  with sort

list1 = [10, 20, 4, 45, 99]

list1.sort(reverse=True)

# printing the first element
print("Smallest element is:", list1[-1])    ## Smallest element is: 4
print("Largest element is:", list1[0])      ## Largest element is: 99


######  3. 'Min' method 

list1 = [10, 20, 1, 45, 99]

# printing the minimum element
print("Smallest element is:", min(list1))    # Smallest element is: 1



########  4.  Find the smallest element in list comparing every element

l=[ int(l) for l in input("List:").split(",")]
print("The list is ",l)

min1 = l[0]

for i in range(len(l)):

	# If the other element is min than first element
	if l[i] < min1: 
		min1 = l[i] #It will change

print("The smallest element in the list is ",min1)

# List:77,83,29,333,3356
# The list is  [77, 83, 29, 333, 3356]
# The smallest element in the list is  29



#######   5. Lambda function

lst = [20, 10, 20, 15, 100, 22]
print(min(lst, key=lambda value: int(value)) )   ## 10


##########    6. Reduce function

from functools import reduce

lst = [20, 7, 20, 15, 100]
print(reduce(min,lst) )      # 7












