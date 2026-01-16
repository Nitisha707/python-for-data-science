import operator
from wsgiref.util import shift_path_info
import turtledemo
print(""""hello
# i'am nitisha sharma
# this is my first program""")
# #""" this is used to change line
# #\n is also used for change line
# #variables
a="hello"
print(a)
# #for space _is used or
evennum=2
even_num=2
num1=2
#data type
#input string""
name=input("what is your name")
print(name)
# #int
age=int(input("how old are you?"))
print(age)
# #float
age=float(input("how old are you?"))
print(age)
length=float(input("how long are you?"))
print(length)
#for addition
exp1=(input("enter your equation"))
print(exp1)
#typecasting and subtypes
name="nitisha sharma"
print(type(name)) age=23
print(type(age))
a=123
b=1.23
print(type(a))
print(type(b))
c=a+b
print(c)
print(type(c))
#conversion
a=int(a)
print("after conversion",type(a))
#swaping variable
#method1
x=12
y=13
temp=x(12)
x=y(13)
y=temp(12)
#method2
x=12
y=13
#left,right=right,left
a,b=b,a
print(b)
print(a)
#convert float into integer
x=12.4
print(type(x))
x=int(x)
print(type(x))
print(x)
#int into float
a=int(input("enter a number"))
print(a)
print(type(a))
a=float(a)
print("after conversion",a)
print(type(a))
#operators and operants
# (+)addition
# (-)subtraction
# (*)multi
# (//)floor division
# (/)division
# (**)exponential
# (%)modulus
##assignment operators
#=
#+=
#-=
#*=
##(+=)
#score=score+1    scre+=1
#score=score-5    score-=5
#score=score*3    score*=3
#identity operators
#is #is not
#is
a=123
b=123
print(a is b) = true
#is not
a=123
b=123
print(a is not B) = false
# bitwise operators
# 1 AND (&) operator
# 2 OR (|) operator
# 3XOR (^) operator
# 4 << zero fill left shift
# 5 >> zero fill right shift
print(bin(15))
# #
a=10
b=8
print(a&b)
# conditional statement
# if the statement is true
marks=97
if marks>=90:
    print('you will get a mobile phone')
    print("thank you")
# #if else statement
else:
    print('you will not get a mobile phone')
    print("thank you")
#if-elif-else
marks=50
if marks>=90:
    print('you can go on a trip')
elif marks>=80 and marks<90:
    print('you will get a new phone')
elif marks>=70 and marks<80:
    print('you will get a new book')
else:
    print("you will not get your phone back")

#nested if statement
marks=96
if marks>=80:print("you will get a new phone")
if marks>=95:
  print("you can go on a trip")
else:
   print("no phone for a month")

#short Hand if statement
marks=98
if marks>=90: print("you will get a phone")

#SHORT HAND IF-ELSE STATEMENT
marks=97
print("you will go to the trip") if marks>=90 else print("no phone")


#write a program to check if a number is positive
num=int(input("Enter a number: "))
if num<0: print("the number is negative")
elif num>=0: print("the number is positive")

#write a program to check whether a number is even or odd
num=int(input("Enter a number: "))
if num % 2 == 0:
    print(num,"is an even number.")
else:
    print(num,"is an odd number.")

#write a program to create area calculator
print("********AREA CALCULATOR********")
print("""press 1 to get the area of square
press 2 to get the area of rectangle
press 3 to get the area of circle
press 4 to get the area of triangle""")
#
choice=int(input("enter a number between 1 and 4: "))

if choice==1:
    side=float(input("enter the side length of one side: "))
    area=side**2
    print("the area of square is",area)
elif choice==2:
    length=float(input("enter the side length of the rectangle: "))
    width=float(input("enter the width of the rectangle: "))
    area=length*width
    print("the area of square is",area)
elif choice==3:
    radius=float(input("enter the radius of the circle: "))
    area=((22/7)*(radius**2))
    print("the area of circle is",area)
elif choice==4:
    base=float(input("enter the base of the triangle: "))
    height=float(input("enter the height of the triangle: "))
    area=0.5*base*height
    print("the area of triangle is",area)
else:
    print("invalid input")


#write a program check the letter is vowel or not
letter=input("enter a letter here:")
if (letter in "aeiou") or (letter in "AEIOU"):
    print("it is a vowel")
else:
    print(" it is not a vowel")


#Write a program to check if a number is a single digit number ,
#2-digit number and so on .....up to 5 digits.
num=int(input("Enter a number here up to 5 digits: "))
if num>=0 and num<=9:
    print("it is single digit number")
elif num>=10 and num<=99:
    print("it is double digit number")
elif num>=100 and num<=999:
    print("it is triple digit number")
elif num>=1000 and num<=9999:
    print("it is four digit number")
else:
    print("it is five digit number")

#loops and types
#for loop
for i in range(1,6):
    print(i)
# #
for i in range(1,6,2):
    print(i)
# #
for i in range(2,1,6,):
    print(i)
#
#print table
n=int(input("enter the number"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)

#while loop
n=0
while n<=5:
    print(n)
    n=n+1

n=1
a=7
while n<=10:
    print(a,"x",n,"=",a*n)
    n=n+1

n=1
a=int(input("enter a number"))
while n<=10:
    print(a,"x",n,"=",a*n)
    n=n+2

#while true
while True:
     print("hello")
# #
# while True:
    num1=int(input("Enter a number: "))
    num2=int(input("Enter another number: "))
    print(num1+num2)
    repeat=input('do you want to stop the program:')
    if repeat=='yes':
        break

#nested loop
for i in range(1,4):
    for j in range(1,11):
        print(j,end="")
        print()

for i in range (1,6):
    for j in range (1, i+1):
      print(j,end = " ")
      print()

for loop with conditional statement
for i in range(1,11):
    if i == 3:
        print("Thank you")
    else:
        print(i)

for i in range (1,101):
    if i % 8 ==0 and i % 12 == 0:
        print(i)
#while loop
n=1
while n<=10:
    if n==3:
        print("add this to fav")
    else:
        print(n)
        n=n+1

# break and continue statement
for i in range(1,11):
    if i == 5:
        continue
    else:
        print(i)
#
for i in range(1,11):
    if i == 7:
        break
    else:
        print(i)

#write a program to find a sum of all the even number up to 50
sum=0
for i in range(1,51):
    if(i%2==0):
        sum=sum+i
        print("the sum of all the even numbers is:",sum)
#
# #write a program to write first 20 number and their square number
for i in range(1,21):
    print(i,i*i)


#write a program to find sum of first odd number
#using while loop
sum=0
n=0
while n <=20:
    if n % 2 !=0:
        sum=sum+n
        n=n+1
        print ('the sum of first 10 odd number is',sum)


#write a program to check if a number is divisible by 8 and 12 up to 100 numbers
for i in range (1,100):
    if i % 8 ==0 and i % 12 == 0:
        print(i)

#write a program to create a billing system at supermarket
while True:
    name=input("Enter customer's name: ")
    total=0
while True:
    print("enter the amount and quantity")
    amount=float(input("enter the amount: "))
    quantity=float(input("enter the quantity: "))
    total=total+amount*quantity
repeat=input("Do you want to add more items? (yes/no): ")
if repeat=="no" or repeat=="NO":
    break
    print("-"*40)
    print("name:",name)
    print("amount to be paid:",total)
    print("-"*40)
    print("*********happy shopping*********")
repeat1=input("Do you want to go to next customer? (yes/no):" )
if repeat1=="no" or repeat1=="NO":
      break

 # a="why fit in,when you are born to stand out !"
#write a program to find the length of the following string
b=(len(a))
print("the length of the string is ",b)
#
print (len (a))

# write a program to check how many times alphabet o is occurring
a="why fit in, when you are born to stand out!"
print(a.count("o"))

# write a program to convert the whole string into lower and upper cases
x=a.lower()
print(x)
y=a.upper()
print(y)
#
# # covert follow stringinto title
z=a.title()
print(z)
#
# # to find index number of "fit in".
print(a.find("fit in"))

# to create a pattern
for i in range (1,6): #for row
    for j in range (1,i+1): #for columns
        print(i,end=" ")
        print()
# #
for i in range (1,6):
    for j in range (6,i+1):
        print(j,end=" ")
print()

for i in range(1,6):
    for j in range(6,i,-1):
      print(j,end=" ")
print()
#

for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end=" ")
        for k in range (i):
            print("*",end=" ")


for i in range (1,6):
    for j in range (i,0,-1):
        print(j,end=" ")
        print()


for i in range (1,6):
    for j in range (1,i,+1):
        print("*",end=" ")
        print()
for i in range (5,0,-1):
    for k in range (0,i,-1):
        print("*",end=" ")
        print()

for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=" ")
        print()


#string manipulation
a=("hello world")
print(type(a))
print(a)
#for find length of string
print(len(a))
#for count the cherecter in string
print(a.count("h"))
#for convert in upper case
print(a.upper())
#for lower
print(a.lower())
#to find index
print(a.index("h"))
#convert first letter into capital
print(a.capitalize())
#convert into lower case
print(a.casefold())
# #
print(a.title())
#to find index
print(a.find("h"))
to write variable inside a string
name="john"
age=18
b="my name is {} . and my age is {}"
print(b.format(name,age))
#it fiils the given string and centralizes a string
print(name.center(50,"*"))

#string functions
a="hello"
b="Hello123"
c="12345"
d="HELLO"
e=" "
f="hello 123@"
g="1.234"
#isalnum - return true if all character in the string are alphanumaric
print(a,a.isalnum())
print(b,b.isalnum())
print(c,c.isalnum())
print(d,d.isalnum())
print(e,e.isalnum())
print(f,f.isalnum())
print(g,g.isalnum())

#isalpha - return true if all character in the string are in the alphabet
print(a,a.isalpha())
print(b,b.isalpha())
print(c,c.isalpha())
print(d,d.isalpha())
print(e,e.isalpha())
print(f,f.isalpha())
print(g,g.isalpha())

#isdecimal - return true if all character in the string are decimal
print(a,a.isdecimal())
print(b,b.isdecimal())
print(c,c.isdecimal())
print(d,d.isdecimal())
print(e,e.isdecimal())
print(f,f.isdecimal())
print(g,g.isdecimal())

#isdigit - return true if all the characters in the string is digits
print(a,a.isdecimal())
print(b,b.isdecimal())
print(c,c.isdecimal())
print(d,d.isdecimal())
print(e,e.isdecimal())
print(f,f.isdecimal())
print(g,g.isdecimal())

#isnumeric - return true if all the character in the string is numeric
print(a,a.isnumeric())
print(b,b.isnumeric())
print(c,c.isnumeric())
print(d,d.isnumeric())
print(e,e.isnumeric())
print(f,f.isnumeric())
print(g,g.isnumeric())

#islower - convert string into lower case
print(a,a.islower())
print(b,b.islower())
print(c,c.islower())
print(d,d.islower())
print(e,e.islower())
print(f,f.islower())
print(g,g.islower())

#isupper
print(a,a.isupper())
print(b,b.isupper())
print(c,c.isupper())
print(d,d.isupper())
print(f,f.isupper())
print(g,g.isupper())

#isspace - return true value if all the characters in string are whitespace
print(a,a.isspace())
print(b,b.isspace())
print(c,c.isspace())
print(d,d.isspace())
print(e,e.isspace())
print(f,f.isspace())
print(g,g.isspace())

#istitle- string follow the rules of title first character should bhi upper case
print(a,a.istitle())
print(b,b.istitle())
print(c,c.istitle())
print(d,d.istitle())
print(e,e.istitle())
print(f,f.istitle())
print(g,g.istitle())

# #endswith() - return true if the string end with specific value
a="Harry potter"
print(a.endswith("t",6,9))

#startswith() - return true if the string starts with specific value
a="harry porter"
print(a.startswith("p",6,9))

#swapcase(0 - swap case, lower case become upper case and vise versa
a="Harry Porter"
print(a.swapcase())

#strip()- return a trimmed version of string
a="    ***   harry  porter ......"
print(a.strip(" * , . "))

#spliit() - splits the string at the specific separator and return a list
a="#OFF#BRB#OMW"
print(a.split("#"))

#ljust() - return a left justified version of the string
a="harry potter"
x=a.join(20,"*")
print(x,"is my fav movie")

#rjust() - return a right justified version of the string
a="harry potter"
x=a.rjust(25,"$")
print(x,"is my fav movie")

#replace() - replace with specific value
a="my name is john"
print(a)
print(a.replace("john","lisa"))

#rindex()- search the string for a specific value and
# return the last position of where it wa found
a="harry potter and the prisoner of azkaban"
print(a.rindex("prisoner"))

#rfind() - search the string for a specific value and returns
#the last position of where it was found
a="harry potter and the goblet of fire"
print(a.rfind("potter"))
#
a="bibidy bobidy boo"
print(a.rfind("dy",6,20))


#slicing in string
a="harry potter and the goblet of fire"
b="0123456789"
print(a[0:5])
print(a[6:12])
print(a[:5])
print(a[6:])
print(a[-4:])
print(b[::2])
print(b[:7:2])
print(b[::-1])
print(b[6::-2])

#write a program to get fibonacci series up to 10 numbers
#fibonacci series
a=0
b=1
n=int(input("enter no."))
if n==1:
    print(1)
else:
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)

#write a program to check if a number is prime or not
num=int(input("enter no."))
if num<=1:
    print("it is not a prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print("it is not a prime number")
            break
        else:
            print("it is prime number")

# #write a program to find a palindrome of integers
num=int(input("Enter a number: "))
temp=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
    if rev==temp:
        print("it is palindrome")
        break
    else:
        print("it is not palindrome")

#write a program to create a area calculator
print("*********AREA CALCULATOR*********")
while True:
    print("""press 1 to get the area of square
    press 2 to get the area of rectangle
    press 3 to get the area of triangle
    press 4 to get the area of circle""")
    choice=int(input("enter a number between 1 and 4: "))
    if choice==1:
        while True:
            side=float(input("enter the side of square: "))
            area=side*side
            print("area of square =",area)
            repeat=input("do you want to continue? (y/n): ")
            if repeat=="n":
                break
    elif choice==2:
             length=float(input("enter the length of rectangle: "))
             width=float(input("enter the width of rectangle: "))
             area=area+length*length
             print("area of rectangle =",area)
             repeat=input("do you want to continue? (y/n): ")
             if repeat=="n":
                break
    elif choice==3:
                while True:
                    base=float(input("enter the base of triangle: "))
                    height=float(input("enter the height of triangle: "))
                    area=0.5+height*base
                    print("area of triangle =",area)
                    repeat=input("do you want to continue? (y/n): ")
                    if repeat=="n":
                        break
    elif choice==4:
                        radius=float(input("enter the radius of circle: "))
                        area=((22/7)*(radius**2))
                        print("area of circle =",area)
                        repeat=input("do you want to continue? (y/n): ")
                        if repeat=="n":
                            break


#A="OOT.YOLO.ASAP.BRB.GTG.OTW"
#WRITE A PROGRAM TO SEPARATE THE FOLLOWING STRING
#ONTO A COMA(,) SEPARATE VALUE
a="OOTD.YOLO.ASAP.BRB.GTG.OTW"
b=a.split(".")
print(b)

#write a program to sort string alphabetically in python
a=input("enter anything here")
b=sorted(a)
print(b)

#write a program to remove a given character from a string
a="hello world"
b=a.replace("e ","-")
print(b)

#WRITE A PROGRAM TO REMOVE DOT(.) FROM A STRING
z="F.R.I.E.N.D.S"
b = z.replace("."," ")
print(b)

#write a program to check the number of occurrence of a substring in a string
a="she sells seashells on the sea shore"
b=a.count('sea')
print("the number of times substring sea is occurring is",b)


#NUMPY
# modules

#datetime module
import datetime
x=datetime.datetime.now()
print(x)
y=datetime.datetime(1997,10,14)
print(y.strftime("%m/%d/%Y"))
print(y.strftime("%A"))
# #
import datetime
print(datetime.datetime.today())

#RANDOM module
import random
l=["heads","tails"]
x=random.choice(l)
# x=random.randint(1,8)
print(x)

#math module
import math
x=max(13,67,15)
print("tha maximum value is",x)
y=min(13,67,15)
print("tha minimum value is",y)
# #power
a=pow(2,4)
print(a)
# #square root
b=math.sqrt(49)
print(b)
# #absolute
c=abs(-12.35*3)
print(c)
# #aprox
k=math.ceil(1.5)
print(k)
m=math.floor(1.5)
print(m)

#creation of modules
import demo01 as demo
a=demo.add(2,3)
print(a)

#numpy array
import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)
print(type(arr))

#slicing
import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr[0:3])
# print(arr[:5])
print(arr[0,3:5])
print(arr[1,3:5])
print(np.shape(arr))
print(np.size(arr))
print(np.ndim(arr))
print(arr.dtype)


#a.shape- array dimensions
#len(a)-length of array
#b.ndim- number of array dimensions
#e.size - number of array elements
#b.dtype - data type of array elements
#b.astype(int) - convert on array to a different type


print(type([1,2,3]) is list)


# ------------------------------
# 📘 Step 1: Python Basics
# ------------------------------
a = 5
b = 3
print("Sum:", a + b)
print("Product:", a * b)

numbers = [10, 20, 30]
for n in numbers:
    print("Number:", n)
