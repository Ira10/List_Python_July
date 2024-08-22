#### 21st and 22nd August, MIT Ana Bell 10

def make_ordered_list(n):
    """ n is a positive int
    Returns a list containing all ints in order 
    from 0 to n (inclusive)
    """
    L = []
    for i in range(n+1):
        L.append(i)
    return L

print(make_ordered_list(6))  # prints [0, 1, 2, 3, 4, 5, 6]


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
# What's the value of brunch here?  ['bacon', 'eggs', 'juice', 'toast', 'jam'] 

# brunch  ['bacon', 'eggs']
# 4303533056  id
# L1  ['bacon', 'eggs', 'juice']
# 4303533056  id
# brunch  ['bacon', 'eggs', 'juice']
# 4303533056  id
# brunch  ['bacon', 'eggs', 'juice', 'toast', 'jam'] 




#######################################
############ AT HOME ###############
#######################################
## Question 3. 
def apply_to_each(L, f):
    """ L is a list of numbers 
        f is a list that takes in a number and returns a number
    Mutate L such that you apply function f to every element in L """
    # your code here
    for i in range(len(L)):
        L[i] = f(L[i])
    return L



test = [1,-2,3]
apply_to_each(test, lambda x: x**2)
print(test)   # prints [1,4,9]

test = [-7, 8, 5, -8, -3]
apply_to_each(test, abs)
print(test)   # prints [7, 8, 5, 8, 3]
