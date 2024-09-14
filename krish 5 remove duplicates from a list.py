### 14th sep   my sol

def duplicate_removal():      ### 3 mins
    L = [1,2,3,4,6,5,1,2,2,8,3,9,10,11,5,6]
    L_new = []

    for i in L:
        if i not in L_new:
            L_new.append(i)
    
    return L_new

print(duplicate_removal())  # [1, 2, 3, 4, 6, 5, 8, 9, 10, 11]

### krish sol

def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1,2,3,4,6,5,1,2,2,8,3,9,10,11,5,6]))  # [1, 2, 3, 4, 6, 5, 8, 9, 10, 11]

Note: This method will not maintain the original order of the list. ['set']
To maintain the order, you can use a loop or a list comprehension.

