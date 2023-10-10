print("hell this is ")
print('this is hell')
print("""go to hell """)

letter ="no one want you know"
print(letter)
print(type(letter))

intger = 2
print(type(intger))

# rules for declaring var name 
# a-z, A-z , 0-9,_
# Can't start form numeric value
# we cant use reserved keywords of py

                        # ***********************MEMORY LOCATION*********************

number = 0
print(id(number))                   

number2 = 0
print(id(number2))  

# means they are pinting at the same memory location
# if the var name is differnt but the value of that vars is same then it stores in the same adress value

number2 = 6
print(id(number2))  

# OPERATORS
# 1. ARITHMATIC OPERATORS =>  +,-,*,/,//,%,**
# 2. relational operators => == , > , < , <= , ~=
# 3. Bitwise operators => & , | , ~ , ^ , << , >>
# 4. assignment operators => = , += , -= , /= , //= , %= , **= , &= , |= , <<= , >>=
# 5. uninary operators are missing in python i++ , --i

# CONDITIONAL STATEMENT

# 1. if statement
me = 10

if me%2==0:
    print("NUMBER IS EVEN")
else:
    print("NUMBER IS ODD")

# 2. elif statement

me = -10

if me<0:
    print("number is negative")
    
elif me%2==0:
    print("NUMBER IS EVEN")
     
else:
    print("NUMBER IS ODD")

a,b,c = 10,20,30

if a>b and b>c:
    print(a)
elif b>c and b>a:
    print(b)
elif c>a and c>b:
    print(c)
else:
    print("thankyou")

# INPUT
a = input()
b = input()
c = input()

if a>b and b>c:
    print("greatest number is")
    print(a)
elif b>c and b>a:
    print("greatest number is")
    print(b)
elif c>a and c>b:
    print("greatest number is")
    print(c)
    
    print("thankyou")
    
#typecasting

a = int(input())
b = int(input())
c = int(input())

# defualt it stores every value as a string

if a>b and b>c:
    print("greatest number is")
    print(a)
elif b>c and b>a:
    print("greatest number is")
    print(b)
elif c>a and c>b:
    print("greatest number is")
    print(c)
    
    print("thankyou")

# defualt it stores every value as a string so the vlue of x will be conactinated value of b and c 
a = input()
b = input()
c = input()
x = b + c

print(x)


