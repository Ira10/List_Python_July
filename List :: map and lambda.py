# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
# result = map(lambda x: x + x, numbers)
result = (lambda x: x + x, numbers)
print(list(result))

y = lambda x : x + x 
print(y(2))
print(y(numbers))



numbers = (1, 2, 3, 4)
result = (lambda x: x + x, numbers)
print(list(result))  # [<function <lambda> at 0x100ac91f0>, (1, 2, 3, 4)]



numbers = (1, 2, 3, 4)
result = lambda x: x + x
print(list(result(numbers)))  # [1, 2, 3, 4, 1, 2, 3, 4]



numbers = [1, 2, 3, 4]
result = lambda x: x + x
print(list(result(numbers)))  # [1, 2, 3, 4, 1, 2, 3, 4]



numbers = [1, 2, 3, 4]
result = lambda x: x + x
print(list(map(result,numbers))) # [2, 4, 6, 8]




numbers = (1, 2, 3, 4)

y = lambda x : x + x 
print(y(2))           # 4
print(y(numbers))     # (1, 2, 3, 4, 1, 2, 3, 4)
print(map(y,numbers)) # <map object at 0x100d1d160>
print(list(map(y,numbers)))  # [2, 4, 6, 8]