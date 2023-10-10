# today we gonna understand list in py 
# syntax
# it is possible to create list under list ie nested list

# list_name = ['hello', 'i ' , 'am ', 'utsav' , 'jaiswal'] check check
# print(list_name)
    
# index just like an array 
list_name = [1,2,3,4]

# it is possible to create list under list ie nested list
print(list_name)
# print all vlaue of list 
print(list_name[:])
# count index from the left side of a list
print(list_name[1])
# count index from the left side of a list
print(list_name[-2])
# not inc. last given value index but left side inc. 
print(list_name[0 : 2])

# print upto last but we here define the initital index of the list 
print(list_name[2:])

# list_up step value 
list_name2 = [1,2,3,4,5,6,7,8,9]
print(list_name2[1::2]) # str value : end vlue : step vlue 

list_name.remove(2) # it remove the exact elemnet from an list not  from the index of A list
print(list_name)

list_name.pop(2) # it pop out the element form the index of that list 
print(list_name)

list_name = [1,2,3,4,5,6,7,8,9] # this will also work as same as pop but not same as remove
del list_name[8]
print(list_name)

# APPEND 

list_0 = [1,2,3,4,5,6,7,8,9]
list_0.append(0)
list_0.append("utsav")
list_0.append([12,13,14,15]) # it appends or you can say ( + ) all the list elements

print(list_0)

# list insert
list_0 = [1,2,3,4,5,6,7,8,9]
list_0.insert(3, 10) # after which index you want to , insert the new element 
print(list_0)

# list extend you can also use + 
list_0 = [1,2,3,4,5,6,7,8,9]
list_0.append(0)
list_0.append("utsav")
list_0.extend([12,13,14,15]) #extend appends the list elemnet not in the form of list but in the form ofr elements

print(list_0)

# sorting 
list_0 = [3,562,3,5,2,67,2,566,64567]
list_0 = sorted(list_0)
print(list_0)

#sort used for dec.

# identity operator
list_0 = [1,2,3,4,5,6,7,8,9] 
list_1 = list_0
print(list_0 is list_1) 

list_1 = list_0.append(5)
print(list_0 is list_1)

# membership operator
list_0 = [1,2,3,4]
print(3 in list_1) # return true if 3 is in the list_1
print(3 not in list_1) # return false if 3 is in the list_1

# for loop' 

for i in range( 1, 10): #10 is in open bracket always
    print(i)
    i += 1
    
# break continue chindi topic hai koi bhi karleg

# 2-d matrix by for loop in range easily set that 

# tuples --> immutable indexed data str
# creation
t = () # --> empty tuple in tuples , important but not parenthesisi
t = (1,2,3)
print(t)

t = (1,2,3,4.4, "hello" , 0.0002 , [1,2,3] , (1,2,3))
print(t)# 2-d matrix by for loop in range easily set that 

# you can do slicing operations in tuples

# del t   it delte the entier tuple

# we cant change tuple but we can change the value of list items if there is a list in our tupple

t = (1,2,3,4.4, "hello" , 0.0002 , [1,2,3] , (1,2,3)) 
t[-2][0] = 9 # example
print(t)

t[-2].append(10) #c we can append too
print(t)

# sorting in tuples

t = (3,2,1)

# check cehck check check
print(t)

t = "utsav" , "jaiswal"
print(t)
print(type(t))

# functions
t = 1,2,3,4,56,7
print(len(t))
print(min(t))
print(max(t))
print(sum(t))

# while loop conditional statemnet\
def reverseNum(num):
    ans = 0
    while num > 0:
        rem = num%10
        ans = 10*ans + rem
        num /=10
    else:
        return ans

def main(a):
    a = int(input())
    print("before reversing a number")
    print(a)
    reversenumber = reverseNum(a)
    print("after reversing a number")
    print(reversenumber)
    




