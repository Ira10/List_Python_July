# Find sum and average of List in Python

####   1st Oct


#########   Sol 1 

import statistics

L = [4, 5, 1, 2, 9, 7, 10, 8]

print(sum(L))  ## 46
print(statistics.mean(L))  ## 5.75


#########   Sol 2
sum = 0
count = 0
for i in L:
    sum += i 
    count += 1
print(sum)  # 46
print(sum/count)  ## 5.75


len_ = len(L)
print(sum/len_)  ## 5.75

