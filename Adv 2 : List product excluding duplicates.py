# Python 3 code to demonstrate
# Duplication Removal List Product

#### using Naive methods

# getting Product


def prod(val):
	res = 1
	for ele in val:
		res *= ele
	return res


# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : " + str(test_list))

# using naive method
# Duplication Removal List Product
res = []
for i in test_list:
	if i not in res:
		res.append(i)
res = prod(res)

# printing list after removal
print("Duplication removal list product : " + str(res))




##### List comprehension


def prod(val):
	res = 1
	for ele in val:
		res *= ele
	return res


# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : " + str(test_list))

# using list comprehension
# Duplication Removal List Product
res = []
[res.append(x) for x in test_list if x not in res]
res = prod(res)

# printing list after removal
print("Duplication removal list product : " + str(res))




##### Using set() and functools.reduce() [Intermediate]

import functools

functools.reduce(lambda x, y: x*y, set([1, 3, 5, 6, 3, 5, 6, 1]), 1)

print(set([1, 3, 5, 6, 3, 5, 6, 1]))


