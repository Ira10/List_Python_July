L = [3,2,6,8,4,6,2,9]

# ## my solution
# even_num = list(map(lambda x: x % 2 == 0, L))

# even_ = even_num.count(True)

# print(even_num)    # [False, True, True, True, True, True, True, False]
# print(even_)    # 6


# ###   Map diff sol

# is_even = lambda x :1 if x  % 2 == 0 else 0

# res = list(map(is_even,L))
# print(res)      # [0, 1, 1, 1, 1, 1, 1, 0]
# print(res.count(1))    # 6



######   Filter  using fucntion

def is_even(n):
    if n%2 == 0:
        return True 
    else:
        return False


evens = list(filter(is_even,L))

print(evens)   # [2, 6, 8, 4, 6, 2]


######   Filter  using lambda 

evens__ = list(filter(lambda n: n%2==0,L))

print(evens__)   # [2, 6, 8, 4, 6, 2]


#######   Map for multiplying blah blah 

muluu = list(map(lambda n: n + 2, L))

print(muluu)     # [5, 4, 8, 10, 6, 8, 4, 11]
