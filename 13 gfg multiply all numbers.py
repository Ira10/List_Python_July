### Multiply all numbers in a list

###   2nd Oct

### 1. for loop

L = [1,2,3]
cnt = 1 
for i in L:
    cnt *= i 
print(cnt)   ## 6

# # 2. mul function 
from operator import *
L = [1,2,3]
m = 1
for i in L:
    m = mul(i,m)
print(m)    ### 6
 


##  3. math 'prod' func

import math 

L = [1,4,5,6]
print(math.prod(L))  ## 120


####  4. lambda function

# list using lambda function and reduce()

from functools import reduce

list2 = [3, 2, 4]

result2 = reduce((lambda x, y: x * y), list2)

print(result2)  ## 24



#######   5. using itertools.accumulate


from itertools import accumulate
list1 = [1, 2, 3]

result1 = list(accumulate(list1, (lambda x, y: x * y)))

print(result1[-1])   ### 6
