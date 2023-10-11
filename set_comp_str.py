# set --> non-indexed, but muttable is is a hash set data structure

s = set()
print(type(s))

s = {1,2,3,7,5} # indexing not support
print(s)

list_0 = [1,2,34,55]
s = set(list_0)
print(s)

s = { 1,2,31,3,1,2,3,1}
print(s)
# print(s[0]) #eror found set' object is not subscriptable

# adding value
s = set()
s.add(1) ; s.add(2) ; s.add(3)
s.update([1,22,31,4] , {23,234,24,45}) # adding multiple values
print(s)

#remove 
s = {1,2,34,55}
print(s)
s.remove(34)  # if element not found in the set then it throw a error
print(s)

s = {1,2,34,55}
print(s)
s.discard(34) # # if element not found in the set then it isn't gonna throw a error but it return the key as it is 
print(s)

#we can use del to delte whole set but we cant delte a particular element by delte
del s

# function of set 
s1 = {1,2,3,4,5}
s2 = {2,4,6}
print (s1 | s2)
print(s1.union(s2)) # used for union

print(s1 & s2)
print(s1.intersection(s2)) # used for intersection 

print(s1-s2)
print(s1.difference(s2)) # here we subtract the elements s1 from s2

print(s2-s1)
print(s2.difference(s1)) # here we subtract the elements s2 from s1

print(s1^s2)
print(s1.symmetric_difference(s2)) # basicaly it XOR the sets 's1 ^ s2'

# let say you foregt the set dir then just print the list of all methods of set in this case if we type 
print(dir(s1))

# how to use that function then type -->
print(help(s1.symmetric_difference))



# dictionary hashmap/hashtable

#syntax --> key:value,
d = {1:"utsav" , 2:"jaiswal" , 3:[0,8,2,0]}
print(d)
print(type(d))

# d = {"a":12 , "sd":"qoelws" , [1,2,3]:3 , [23,21,13,]:45} #TypeError: unhashable type: 'set' , TypeError: unhashable type: 'list'

#accesing in O(1)
print(d[1]) # it print the value at key but we cant access the key by value and threw a error when the key not found 

d[4] = "master" # inserting a key vlaue pair in dic 
print(d)

# as we know hashmap derived from hash so all the basic function which we already learn in the set immplies in dictionary too

#get method --> doesnt throw an error

print(d.get(5))
print(d.get(3))
print(d.get(1))

# pop and pop items

print(d.pop(2))
print(d)

print(d.popitem()) # randomly removes just like pop in set
print(d)

#update

d1 = { 1:2 , 2:3 , 3:4 , 4:5}
print(d1)
print(d1.items())

for items in d1.items():
    print(items)

for v in d1.values():
    print(v)
    
#deafaut key is used to set the initialize the vlaue of key first at zero

#dictinary comprehension]
d2 = {}

for a, b in d1.items():
    d2[a] = b*b
print(d2)

# string 
s = "hello"
print(s)

#methods in string all methods are too basic go to dir(string) and if you find any doubt then just use help command

#check whether the given word of sting is palindrome or not
def Checkpl(str1 , length , index):
  
    length = len(str1) -1 
    index = 0

    while index < length:
        if(str1[index] == str1[length]):
            index = index + 1
            length = length -1
    
        else:
            return 0
    
    return 1

str1 = "madam"
length = len(str1)
index = 0

ans = Checkpl(str1 , length , index)

if ans == 1:
    print(str1 , " is a palindrome")
else:
    print(str1 , " is a not palindrome")
