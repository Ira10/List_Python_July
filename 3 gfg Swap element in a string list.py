#### Not my solution, didn't understand the question, gfg's solutions  ## 25th Aug

# method #1 : Using replace() + list comprehension   

# Initializing list
test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

# printing original lists
print("The original list is : " + str(test_list))

# Swap elements in String list
# using replace() + list comprehension
res = [sub.replace('G', '-').replace('e', 'G').replace('-', 'e') for sub in test_list]

# printing result 
print ("List after performing character swaps : " + str(res))





#  Method #2 : Using join() + replace() + split()

# Initializing list
test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

# printing original lists
print("The original list is : " + str(test_list))

# Swap elements in String list
# using replace() + join() + split()
res = ", ".join(test_list)
print(test_list)
print(res)
res = res.replace("G", "_").replace("e", "G").replace("_", "e").split(', ')

# printing result 
print ("List after performing character swaps : " + str(res))

