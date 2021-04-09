
import math
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def sqrt(a):
    result=math.sqrt(a)
    return result

def exp(a):
    return a**2

def sin(x):
    result=math.sin(x)
    return result

def cos(x):
    result=math.cos(x)

def tan(x):
    result=math.tan(x)

#choosing the operation
print("""
Choose a number for the following operations
1-Addition(x,y)
2-Subtraction(x,y)
3-Multiplication(x,y)
4-Divide(x,y)
5-Square(x)
6-Square root(x)
7-sin(x)
8-cos(x)
9-tan(x)""")
op=int(input('What operation do you want to perform?'))

while op<10:
    if op==1:
        print('enter the paramaters')
        x1=int(input('Enter x'))
        y1=int(input('Enter y'))
        res1=add(x1,y1)
        print('Addition=',res1)
    elif op==2:
        x2=int(input('Enter x'))
        y2=int(input('Enter y'))
        res2=subtract(x2,y2)
        print('Subtraction=',res2)
    elif op==3:
        x3=int(input('Enter x'))
        y3=int(input('Enter y'))
        res3=multiply(x3,y3)
        print('Multiplication=',res3)
    elif op==4:
        x4=int(input('Enter x'))
        y4=int(input('Enter y'))
        res4=divide(x4,y4)
        print('Division=',res4)
    elif op==5:
        x5=int(input('Enter x'))
        y5=int(input('Enter y'))
        res5=pow(x5,y5)
        print('Exponent=',res5)
    elif op==6:
        x6=int(input('Enter x'))
        res6=sqrt(x6)
        print('square root=',res6)
    elif op==7:
        x7=int(input('Enter x'))
        res7=sin(x7)
        print('sin(x)=',res7)
    elif op==8:
        x8=int(input('Enter x'))
        res8=cos(x8)
        print('cos(x)=',res8)
    elif op==9:
        x9=int(input('Enter x'))
        res9=tan(x9)
        print('tan(x)=',res9)
    else:
        print('Choose another operation')
    new=int(input('do you want to continue?-(yes-1),(no-0)'))
    if new==1:
        op=int(input('Enter operation'))
    elif new==0:
        print('Thanks for using the scientific calculator')
        break







