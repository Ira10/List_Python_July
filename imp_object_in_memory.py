# def make_ordered_list(n):
#     """ n is a positive int
#     Returns a list containing all ints in order 
#     from 0 to n (inclusive)
#     """
#     L = []
#     for i in range(n+1):
#         L.append(i)
#     return L

# print(make_ordered_list(6))  # prints [0, 1, 2, 3, 4, 5, 6]


# Question 2
L1 = ['bacon', 'eggs']
L2 = ['toast', 'jam']
brunch = L1
print("brunch ",brunch)
print(id(brunch), " id")
L1.append('juice')

print("L1 ", L1)
print(id(L1), " id")

print("brunch ", brunch)
print(id(brunch), " id")


brunch.extend(L2)
print("brunch ",brunch)
# What's the value of brunch here?   
