##########    14th Oct

########    1.  For Loop 

list1 = [10, 21, 4, 45, 66, 93]

for num in list1:

    if num % 2 == 0:
        print(num)   ##, end=" ")


#####   2. While Loop
        
list1 = [10, 24, 4, 45, 66, 93]
num = 0

while(num < len(list1)):

    if list1[num] % 2 == 0:
        print(list1[num]) ##, end=" ")

    # increment num
    num += 1



#####  3. List Comprehension

list1 = [10, 21, 4, 45, 66, 93]

even_nos = [num for num in list1 if num % 2 == 0]

print("Even numbers in the list: ", even_nos)


#####   4. Lambda Expression 


list1 = [10, 21, 4, 45, 66, 93, 11]

even_nos = list(filter(lambda x: (x % 2 == 0), list1))

print("Even numbers in the list: ", even_nos)



######  5 . Recursion

def evennumbers(list, n=0):

    # base case
    if n == len(list):
        exit()
    if list[n] % 2 == 0:
        print(list[n], end=" ")
    
    # calling function recursively
    evennumbers(list, n+1)

# Initializing list  
list1 = [10, 21, 4, 45, 66, 93]

print("Even numbers in the list:", end=" ")
evennumbers(list1)
