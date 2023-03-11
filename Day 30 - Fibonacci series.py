# Day 30
# To write a program to print the fibonacci series using recursion

fn = 0
fn1 = 1

n = int(input("Enter the number of elements you want\n"))

def fibonacci (n, fn, fn1):
    if (n > 2):
        fn2 = fn1 + fn
        print(fn2)
        fibonacci (n-1, fn1, fn2)
        
if (n == 1):
    print (0)
elif (n == 2):
    print (0)
    print (1)
else:
    print (0)
    print (1)
    fibonacci (n, fn, fn1)