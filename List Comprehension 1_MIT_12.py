########## YOU TRY IT AT HOME #############
## Write a list comprehension expression that uses a list named L.
# It makes a new list whose elements are the middle 
# character of strings whose length is 3. 

def list_com(L):
    Lnew = [e[1] for e in L if len(str(e)) == 3]
    return Lnew


# If L = ['abc', 'm', 'p', 'xyz', '123', 57]
# It makes ['b', 'y', '2']
L = ['abc', 'm', 'p', 'xyz', '123', 57]
print(list_com(L))

# TypeError: object of type 'int' has no len()