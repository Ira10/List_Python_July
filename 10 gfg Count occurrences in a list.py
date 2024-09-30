# Python | Count occurrences of an element in a list
#     30th Sep

#### solution 1 by me

L = [1,2,3,5,4,3,2,234,42,3,3,3,3,2,1]

char_list = ['a','a','b','c','d','e','f','a','a']

print(L.count(3))   ### 6 

print(char_list.count('a'))   ##  4

print("\n")

#### solution 2 by me


what_to_find = 2  #3
count = 0
for i in L:
    if i == what_to_find:
        count+=1
print(count)    ## 3

what_to_find_char = 'a'  #3
count_ = 0
for i in char_list:
    if i == what_to_find_char:
        count_+=1
print(count_)  ### 4


#######   3 . Using List Comprehension
cnt = 0
# count__ = [cnt + 1 for i in L if i == 3]  
count__ = [1 for i in L if i == 3]  ### it's okay even if I don't do cnt+1
print(len(count__))  ## 6    ##### len is very very important
print(count__)  ### [1, 1, 1, 1, 1, 1]



#####    4. Dictionary Comprehension

lis = ['a', 'd', 'd', 'c', 'a', 'b', 'b', 'a', 'c', 'd', 'e']
occurrence = {item: lis.count(item) for item in lis}
print(occurrence.get('a'))  ## 3   # 47 and 51 does the same
for item in lis:
    print(item)
print(occurrence)  # {'a': 3, 'd': 3, 'c': 2, 'b': 2, 'e': 1}
print(occurrence['a']) ## 3   # 47 and 51 does the same



# for item in lis:
#     print(item)
# a
# d
# d
# c
# a
# b
# b
# a
# c
# d
# e
