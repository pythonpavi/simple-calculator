#simple calculator
def add (a,b):
    return a+b
def sub (a,b):
    return a-b
def mul (a,b):
    return a*b
def div (a,b):
    return a/b
print ("""select operation
        1.add
        2.sub
        3.mul
        4.div
        """)
choice = int(input("enter your choice"))
a = int(input("enter the number one"))
b = int(input("enter the number two"))
if choice == 1:
    print(add(a,b))
if choice == 2:
    print (sub(a,b))
if choice == 3:
    print (mul(a,b))
if choice == 4:
    print (div(a,b))
else:
    print ("enter the correct choice")
