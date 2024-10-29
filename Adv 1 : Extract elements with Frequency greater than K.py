##########   29th Oct



##### Method #1 : Using count() + loop


# test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
# K = 2 

# def op(test_list,K):
#     dict = {}
#     new_list = []
#     for i in test_list:
#         if i in new_list:
#             dict[i] = dict[i] + 1
#         else:
#             new_list.append(i)
#     return dict 

# print(op(test_list,K))


test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
K = 2 

def op(test_list, K):
    count_dict = {}  # Rename 'dict' to avoid overwriting the built-in 'dict' keyword
    
    # Count the frequency of each element in test_list
    for i in test_list:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    
    # Filter the elements whose frequency is greater than or equal to K
    result = {key: value for key, value in count_dict.items() if value >= K}
    
    return result

print(op(test_list, K))





dict_ = {4: 4, 6: 3, 3: 3} 
for i in dict_:  ### this gives the value
    print(i)