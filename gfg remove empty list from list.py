########  1. List Comprehenseleon


l = [1,2,3,4,'', [], 8,9]

new = [ele for ele in l if (ele != [] and ele != '')]

print(new) # [1, 2, 3, 4, 8, 9]


# new = [ele for ele in l if (ele != [] or ele != '')] # [1, 2, 3, 4, '', [], 8, 9]

# This condition includes ele in new if either ele != [] or ele != '' is True.
# Since ele cannot be both [] and '' simultaneously, at least one of these conditions will always be True for every element in l.
# This means no elements will be filtered out, resulting in the original list: [1, 2, 3, 4, '', [], 8, 9].
