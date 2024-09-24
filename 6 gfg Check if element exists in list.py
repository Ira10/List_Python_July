############ 19th Sep

#### my sol ### 3 mins

L = [1, 6, 3, 5, 3, 4]

find_ = 3

for i in range(len(L)):
    if L[i] == find_:
        print("True")
# True
# True
        


for i in range(len(L)):
    if L[i] == find_:
        print("True")
        break

# True
    

### 1. 'IN' operator
    
L = [1, 6, 3, 5, 3, 4]

find_ = 3

if find_ in L:
    print("True")  


### 2. any() function
    
# Initializing list
test_list = [1, 6, 3, 5, 3, 4]

result = any(item in test_list for item in test_list)
print("Does string contain any list element : " +str(bool(result)))
print(result)

# Does string contain any list element : True
# True


########  3. count() function

test_list = [1, 6, 3, 5, 3, 4]

count_ = test_list.count(3)

if count_ >=  1:
    print("exists")

# exists


########  4. count() function
# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
# result = map(lambda x: x + x, numbers)
result = (lambda x: x + x, numbers)
print(list(result))

y = lambda x : x + x 
print(y(2))
print(y(numbers))
