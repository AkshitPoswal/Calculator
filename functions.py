def add(x,y):

    print("sum of two n0.s", x+y)
def sub(x,y):
    print("sub of two no. is :", x-y)
def mult(x,y):
    print("Product of two no. is:", x*y)
def div(x,y):
    print("div of two no.:", x/y)
def remnd(x,y):
    print('remender of two no. is:', x%y)


x=int(input('enter the first no.\n'))
y=int(input("enter 2nd no\n"))
z=str(input("for add(+),for sub(-),mult(*),for remnd(%),divide(/)\n"))
if(z== '+'):
    add(x,y)
if(z=='-'):
    sub(x,y)
if(z=="*"):
    mult(x,y)
if(z=='/'):
    div(x,y)
if(z=='%'):
    remnd(x,y)
