### 2nd Oct

from functools import reduce

list2 = [3, 2, 4]

result2 = reduce((lambda x, y: x * y), list2)

print(result2)  ## 24