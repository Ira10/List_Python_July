#### 26th Sep


houses_nested_list = [
    [115910.26, 128.0, 4.0],
    [48718.17, 210.0, 3.0],
    [28977.56, 58.0, 2.0],
    [36932.27, 79.0, 3.0],
    [83903.51, 111.0, 3.0],
]

# for i in houses_nested_list:
#     print(i)
#     for j in i:
#         print(j)

for i in houses_nested_list:
    # print(i)
    i.append(i[0]/i[1])
    print(i)
    # for j in i:
    #     print(j)
#     i.append(i[0]/i[1])

# print(i)