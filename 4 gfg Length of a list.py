################    25th Aug 


######## My solution - 1   ## wrong

# def len_list(*args):
#     for lists_ in args:
#         return len(lists_)
    

# L = list(input("Enter the list : "))

# print(len_list())

# # Enter the list : [1,2,3] [4,5,6] [7,2,1,5,3]
# # None
    
 
# ##############  Solution --- Chatgpt 

# def len_list(*args):
#     lengths = []
#     for lists_ in args:
#         lengths.append(len(lists_))
#     return lengths

# L1 = [1, 2, 3]
# L2 = [4, 5, 6, 7]
# L3 = [8, 9]

# print(len_list(L1, L2, L3))


# #################  Different versions 

# def len_list(*args):
#     lengths = []
#     for lists_ in args:
#         lengths.append(len(lists_))
#     return lengths

# # Taking input for multiple lists
# L1 = list(map(int, input("Enter the elements of the first list separated by space: ").split()))
# L2 = list(map(int, input("Enter the elements of the second list separated by space: ").split()))
# L3 = list(map(int, input("Enter the elements of the third list separated by space: ").split()))

# # Calculating and printing the lengths of the lists
# print("Lengths of the lists:", len_list(L1, L2, L3))

# # Enter the elements of the first list separated by space: 1 2 3 4
# # Enter the elements of the second list separated by space: 4 5 6 7
# # Enter the elements of the third list separated by space: 6 3 42 98 32
# # Lengths of the lists: [4, 4, 5]




#####################   Different Version 


# def len_list(*args):
#     lengths = []
#     for lists_ in args:
#         lengths.append(len(lists_))
#     return lengths

# # Taking input for multiple lists in one variable
# input_data = input("Enter multiple lists separated by semicolons (e.g., 1 2 3; 4 5 6 7; 8 9): ")

# # Splitting the input data into separate lists
# lists = [list(map(int, lst.split())) for lst in input_data.split(';')]

# # Calculating and printing the lengths of the lists
# print("Lengths of the lists:", len_list(*lists))

# # lst = (1,2,3)
# # lists = list(map(int, lst.split()))
# # print(lists)

# # Enter multiple lists separated by semicolons (e.g., 1 2 3; 4 5 6 7; 8 9): 1 2 3; 4 5 6 7; 8 9
# # Lengths of the lists: [3, 4, 2]



################  Different for adding ()

def len_list(*args):
    lengths = []
    for lists_ in args:
        lengths.append(len(lists_))
    return lengths

# Taking input for multiple lists in one variable
input_data = input("Enter multiple lists separated by semicolons (e.g., 1 2 3; 4 5 6 7; 8 9): ")

# Clean up the input data by removing any unwanted characters like '(' and ')'
clean_input_data = input_data.replace('(', '').replace(')', '')

# Splitting the input data into separate lists
lists = []
for lst in clean_input_data.split(';'):
    try:
        # Attempt to convert the split elements to integers and create a list
        clean_list = list(map(int, lst.split()))
        lists.append(clean_list)
    except ValueError as e:
        print(f"Skipping invalid list due to error: {e}")

# Calculating and printing the lengths of the valid lists
print("Lengths of the valid lists:", len_list(*lists))


