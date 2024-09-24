######## 24th Sep


# 1.  My solution :: using 'Clear'

# L = [1,2,3]

# print(L," ")   # [1, 2, 3]  
        

# L.clear()

# print(L)    #   []


#####     2. using '*='

# L = [1,2,3]

# print(L," ")

# L *= 0

# print(L)


#####    3. Using 'pop'


# L = [1,2,3]

# print(L," ")  # [1, 2, 3]  

# L.pop()

# print(L)    # [1, 2]       so need to put a loop to clear it out


#####   4. Using 'del'


L = [1,2,3]

print(L," ")  # [1, 2, 3]  

del(L[:])

print(L)     # []