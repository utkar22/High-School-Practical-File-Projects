def question1():
    fibo=(0,1)
    for a in range (2,9):
        x=fibo[a-2]+fibo[a-1]
        fibo=fibo+(x,)
    print (fibo)

def question2a(x):
    f=(0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584)
    print (f[x-1])


def question2b(x):
    f=(0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584)
    print (f.index(x)+1)

def question3():
    g=()
    for a in range(1,6):
        tu=()
        for b in range(1,4):
            print ("Student",a,"Subject",b)
            x=int(input("Marks? "))
            tu=tu+(x,)
        g=g+(tu,)
    print (g)
    question4(g)

def question4(t):
    tu=()
    for a in t:
        x=0
        for b in a:
            x=x+b
        tu=tu+((x/3),)
    print (tu)
    
def question5():
    a=input("Enter a tuple")
    b=input("Enter another tuple")
    c=a+b
    print (c)

def question6(str_tuple):
    a=min(str_tuple)
    print (a)

def question7a():
    t=tuple()
    for a in range(1,51):
        t=t+((a**2),)
    print (t)
    
def question7b():
    t=tuple()
    for c in range(1,27):
        h=chr(c+96)
        t=t+(h*c,)
    print (t)

def question8():
    t=((2,5),(4,2),(9,8),(12,10))
    n=0
    for x in t:
        a,b=x
        if a%2==0 and b%2==0:
            n+=1
    print (n)

def question9():
    seq_a=input("Enter a tuple")
    seq_b=input("Enter another tuple")
    f=1
    for a in seq_a:
        if a not in seq_b:
            f=0
    if f==0:
        print ("False")
    else:
        print ("True")

def question10(t):
    x=0
    for a in t:
        x+=a
    m=x/len(t)
    return (m)

def question11(t):
    tt=tuple()
    for a in t:
        b=question10(a)
        tt+=(b,)
    m=question10(tt)
    print (m)

def question12(t):
    import math
    m=question10(t)
    n=len(t)
    a=0
    for i in t:
        b=(i-m)**2
        a+=b
    c=a/(n-1)
    S=math.sqrt(c)
    print ("The standard deviation is",S)
