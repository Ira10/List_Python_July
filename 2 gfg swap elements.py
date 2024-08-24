def swap_(L,pos1, pos2):
    L[pos1], L[pos2] = L[pos2], L[pos1]
    return L 


pos1 = int(input("Enter the position 1 : "))
pos2 = int(input("Enter the position 2 : "))
L = list(input("Enter the list : "))

print(swap_(L,pos1, pos2))

# Enter the position 1 : 2
# Enter the position 2 : 5
# Enter the list : 123456789
# ['1', '2', '6', '4', '5', '3', '7', '8', '9']


# Enter the position 1 : 2
# Enter the position 2 : 10
# Enter the list : 798031234567890854321135
# ['7', '9', '6', '0', '3', '1', '2', '3', '4', '5', '8', '7', '8', '9', '0', '8', '5', '4', '3', '2', '1', '1', '3', '5']



##########  take list as input ####

def swap_(L,pos1, pos2):
    L[pos1], L[pos2] = L[pos2], L[pos1]
    return L 


pos1 = int(input("Enter the position 1 : "))
pos2 = int(input("Enter the position 2 : "))
L = input("Enter the list (space-separated): ").split()


print(swap_(L,pos1, pos2))

# Enter the position 1 : 4
# Enter the position 2 : 0
# Enter the list (space-separated): 1 2 4 1 22 4 76 23 233 111 234 56 8 2 03 23 
# ['22', '2', '4', '1', '1', '4', '76', '23', '233', '111', '234', '56', '8', '2', '03', '23']



###############   using pop method  ########

# Python3 program to swap elements
# at given positions

# Swap function
def swapPositions(list, pos1, pos2):
	
	# popping both the elements from list
	first_ele = list.pop(pos1) 
	second_ele = list.pop(pos2-1)
	
	# inserting in each others positions
	list.insert(pos1, second_ele) 
	list.insert(pos2, first_ele) 
	
	return list

# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1, pos2))




# Python3 program Swap Two Elements in a List Using tuple variable

# Swap function
def swapPositions(list, pos1, pos2):

	# Storing the two elements
	# as a pair in a tuple variable get
	get = list[pos1], list[pos2]
	
	# unpacking those elements
	list[pos2], list[pos1] = get
	print(get)
	return list

# Driver Code
List = [23, 65, 19, 90]

pos1, pos2 = 1, 3
print(swapPositions(List, pos1-1, pos2-1))
