########   My solution

test_list = [4, 5, 6, 7, 3, 9]
 
# Initialization of range 
i, j = 3, 10

# print(min(test_list))

min_ = min(test_list)
max_ = max(test_list)

if min_ >= i and max_ <= j:
    print("In range")
else:
    print("Out of range")


#########  All condition 

# Initializing loop 
test_list = [4, 5, 6, 7, 3, 9]

# printing original list 
print("The original list is : " + str(test_list))

# Initialization of range 
i, j = 3, 10

# Test if List contains elements in Range
# using all()
res = all(ele >= i and ele < j for ele in test_list) 

# printing result 
print ("Does list contain all elements in range : " + str(res))



##########   Filter function

# Initializing list and range boundaries
test_list = [4, 5, 6, 7, 3, 9]
i, j = 3, 10

# Function to check if x lies within the given range
def in_range(x):
	return i <= x < j

# Filtering out the elements that lie within the range
filtered_list = list(filter(in_range, test_list))

# Checking if the filtered list is not empty
res = bool(filtered_list)

# Printing the result
print("Does list contain any element in range: " + str(res))

