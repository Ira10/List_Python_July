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


What happens here?
min(lst, key=lambda value: int(value)):
The min() function looks at each number in the list.
# The lambda part is a small "helper" that says, "Hey, treat each number like an integer (whole number)."
# Even though the numbers in the list are already integers, this line is saying, "Let me be sure we compare them as numbers."


##########    6. Reduce function

from functools import reduce

lst = [20, 7, 20, 15, 100]
print(reduce(min,lst) )      # 7


Here’s how it works:

It first looks at the first two numbers: 20 and 50. Which is smaller? 20.
Now, it keeps 20 and compares it with the next number: 77. Which is smaller? 20 again.
Then it compares 20 with 98. Still, 20 is smaller.
But now it compares 20 with 7. Uh-oh! 7 is smaller, so now the machine keeps 7.
It keeps doing this with the rest of the numbers: 7 vs. 20 (7 is smaller), 7 vs. 15 (7 is smaller), 7 vs. 100 (7 is smaller).
At the end, the machine says: "The smallest number in the whole list is 7!"

That's how reduce works: it keeps comparing two numbers at a time until it has gone through the entire list and finds the answer!

So, your code prints 7 because it's the smallest number.












