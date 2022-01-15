def question1():
    x=eval(input("Enter a list of integers "))
    x.reverse()
    print (x)

def question2():
    x=eval(input("Enter a list "))
    y=eval(input("Enter another list "))
    z=x+y
    print (z)

def question3():
    x=eval(input("Enter a list containing the numbers 1 to 12 "))
    y=len(x)
    for a in range(0,y,1):
        if x[a]>10:
            x[a]=10
    print (x)

def question4():
    x=eval(input("Enter a list "))
    y=len(x)
    for a in range(0,y,1):
        z=x[a]
        x[a]=z[1:]
    print (x)

def question5():
    x=list()
    y=list()
    z=list()
    for a in range(0,49,1):
        x.append(a+1)
    for b in range(0,50,1):
        y.append((b+1)**2)
    for c in range(0,26,1):
        h=chr(c+97)
        z.append(h*(c+1))
    print (x)
    print (y)
    print (z)

def question6():
    n=list()
    l=eval(input("Enter a list of integers "))
    m=eval(input("Enter a list of integers with same size as previous list "))
    x=len(l)
    for a in range(0,x,1):
        n.append(l[a]+m[a])
    print (n)

def question7():
    x=eval(input("Enter a list "))
    y=list()
    k=len(x)
    y.append(x[k-1])
    for a in range (0,(k-1),1):
        y.append(x[a])
    print (y)

def question8():
    f=[0,1]
    for a in range (2,21,1):
        f.append(f[a-2]+f[a-1])
    x=int(input("What term of the fibonacchi series do you want? (only till 20) "))
    print (f[x+1])

def question9a():
    x=eval(input("Enter a list "))
    j=len(x)
    l=0
    for a in range(0,j,1):
        k=len(x[a])
        if k>l:
            l=k
            m=x[a]
    print ("The longest string is",m)

def question9b():
    l=eval(input("Enter a list of numbers "))
    num=int(input("What number do you want to add them with?" ))
    x=len(l)
    for a in range(0,x,1):
        l[a]=l[a]+num
    print (l)
