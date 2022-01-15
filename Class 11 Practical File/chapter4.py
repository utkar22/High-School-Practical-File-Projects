def question3():
    a=float(input("Enter a number: "))
    b=float(input("Enter another number: "))
    x=a-b
    if x>-0.001 and x<0.001:
        print ("Close")
    else:
        print ("Not close")

def question4():
    a="Leap year"
    b="Not Leap year"
    y=int(input("Enter year: "))
    if y%400==0:
        print (a)
    elif y%100==0:
        print (b)
    elif y%4==0:
        print (a)
    else:
        print (b)

def question5():
    a=int(input("Side 1: "))
    b=int(input("Side 2: "))
    c=int(input("Side 3: "))
    if a+b>c and b+c>a and c+a>b:
        print ("Triangle will be formed")
    else:
        print ("Triangle will not be formed")

def question6():
    x=int(input("Enter a single digit: "))
    if x==0:
        print ("Zero")
    elif x==1:
        print ("One")
    elif x==2:
        print ("Two")
    elif x==3:
        print ("Three")
    elif x==4:
        print ("Four")
    elif x==5:
        print ("Five")
    elif x==6:
        print ("Six")
    elif x==7:
        print ("Seven")
    elif x==8:
        print ("Eight")
    elif x==9:
        print ("Nine")

def question7(x):
    import math
    f=0
    y=math.sqrt(x)
    z=int(y)
    for a in range (2,z,1):
        if y%a==0:
            f=1 #raises flag that it is divisible by a number
            break
    if z!=y:
        print ("The square root is irrational")
    elif f==0:
        print ("The square root is a prime number")
    else:
        print ("The square root is not a prime number")
        
def question8(n):
    for a in range(((n*2)-1),0,-2):
        print (a)

def question10():
    a=0
    b=0
    n=0
    c=0
    while c!=1:
        a=int(input("Enter a number: (press 9999 to quit) "))
        if a==9999:
            break
        b=b+a
        n=n+1    
    avg=b/n
    print (avg)

def question11():
    a=int(input("Side 1: "))
    b=int(input("Side 2: "))
    c=int(input("Side 3: "))
    if a==b:
        if b==c:
            print ("Equilateral")
        else:
            print ("Isosceles")
    elif a==c or b==c:
        print ("Isosceles")
    else:
        print ("Scalene")

def question12():
    a=int(input("Enter an integer: "))
    if a%10==4 or a%10==8:
        print ("Ends with",(a%10))
    else:
        print ("Ends with neither")

def question13():
    a=int(input("Input a number: "))
    if a>20:
        for b in range (11,(a+1),1):
            if b%3==0 and b%7==0:
                print ("Tipsy topsy")
            elif b%3==0:
                print ("Tipsy")
            elif b%7==0:
                print ("Topsy")
            if b%3!=0 or b%7!=0:
                print (b)
    else:
        print ("bye")

def question14():
    l=0
    c=0
    while c!=1:
       x=int(input("Enter a number: (press 9999 to quit) "))
       if x==9999:
           break
       if x>l:
           l=x
    print ("The largest number is",l)
    
def question15():
    l=list()
    n=int(input("How many numbers do you want to enter? "))
    for a in range(0,n,1):
        m=int(input("Enter a number: "))
        l.append(m)
    l.sort()
    print ("The second largest number is",l[-2])

def question16():
    a=int(input("Enter an integer: "))
    z=str(a)
    l=len(z)
    p=0
    if l%2==0:
        b=l//2
    else:
        b=(l//2)+1
    for x in range(0,b,1):
        if z[x]==z[l-1-x]:
            p=1
        else:
            p=0
            break
    if p==1:
        print ("It is a palindrome")
    else:
        print ("It is not a palindrome")

def question17(x):
    a=str(x)
    n=len(a)
    y=(n*10)+(x//(10**(n-1)))
    print (y)

def question18a():
    s=1
    x=0
    for a in range(0,7):
        x=x+(s*(2+(a*3))/(9+(a*4)))
        s=s*(-1)
    print (x)

def question18b(n):
    x=0
    for a in range(1,(n+1),2):
        x=x+(a**2)
    print(x)

def question22a(x):
    s=1
    y=0
    for a in range(1,7,1):
        f=1
        for b in range(1,(a+1),1):
            f=f*b
        y=y+(s*((x**a)/f))
        s=s*(-1)
    print (y)
    
def question22b(x,n):
    y=0
    for a in range(1,(n+1),1):
        y=y+((x**a)/a)
    print (y)

def question23a():
    for a in range(-2,3,1):
        if a<0:
            i=-a
        else:
            i=a
        print(" "*(i),"* "*(3-i))

def question23b():
    for a in range(-3,4,1):
        if a<0:
            a=-a
        a=3-a
        for h in range(1,(a+1),1):
            print("*",end=" ")
        print (" ")

def question23c():
    for a in range(-2,3,1):
        if a<0:
            i=-a
        else:
            i=a
        print((" "*i),("*"+(" "*(3-(2*i))))*(2-(i//2)))

def question23d():
    for a in range(-3,4,1):
        if a<0:
            i=-a
        else:
            i=a
        if i==3:
            x=1
        else:
            x=2
        print (("*"+(" "*(2-i)))*x)

    
def question26(a,b,c):
    if a>b:
        if a>c:
            x=a
            if b>c:
                y=b
                z=c
            else:
                y=c
                z=b
        else:
            x=c
            y=a
            z=b
    elif b>a:
        if b>c:
            x=b
            if a>c:
                y=a
                z=c
            else:
                y=c
                z=a
        else:
            x=c
            y=b
            z=a
    print ("Smallest number =",z)
    print ("Next highest number =",y)
    print ("Highest number =",x)

def question27():
    t1=int(input("Enter a temperature: "))
    s=input("Enter temperature scale: (C/F) ")
    if s=="C":
        t2=((9/5)*t1)+32
    else:
        t2=(5/9)*(t1-32)
    print (t2)
        
    
