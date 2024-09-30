# Python | Count occurrences of an element in a list
#     30th Sep

#### solution 1 by me

L = [1,2,3,5,4,3,2,234,42,3,3,3,3,2,1]

char_list = ['a','a','b','c','d','e','f','a','a']

print(L.count(3))

print(char_list.count('a'))

print("\n")

#### solution 2 by me


what_to_find = 2  #3
count = 0
for i in L:
    if i == what_to_find:
        count+=1
print(count)

what_to_find_char = 'a'  #3
count_ = 0
for i in char_list:
    if i == what_to_find_char:
        count_+=1
print(count_)
