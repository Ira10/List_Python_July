## Sum of number digits in List

## 1st Oct

# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]

L = [12, 67, 98, 34]

new_L =[]
for i in L:
    # print(i)
    cnt = 0
    for j in str(i):
        # print(j)
        cnt += int(j)
        # print(cnt)
# cnt=0
    new_L.append(cnt)

print(new_L)  ## [3, 13, 17, 7]
