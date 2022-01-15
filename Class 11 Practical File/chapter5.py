def question1():
    x=input("Enter a phone number with proper format (eg- /'017-555-1212/'): ")
    a=x[3]+x[7]
    b=x[:3]+x[4:7]+x[8:]
    if len(x)==12:
        print ("It is a valid format")
        if a=="--" and b.isdigit():
            print ("It is a valid phone number")
        else:
            print ("However, it is an invalid phone number")
    else:
        print ("It is an invalid format")

def question2():
    x=input("Enter a string: ")
    print ("The original string is:",x)
    y=len(x)
    c=0
    f=0
    for a in range(0,y,1):
        z=x[a]
        if z.isdigit():
            print(z, end="")
            b=int(z)
            c=c+b
            f=1
    if f==0:
        print("has no digits")
    else:
        print (" ")
        print (c)

def question3():
    x=input("Enter some sentences: ")
    y=len(x)
    an=0
    w=1
    for a in range(0,y,1):
        if x[a].isspace():
            w=w+1
        elif x[a].isalnum():
            an=an+1
    print ("There are",w,"words")
    print ("There are",y,"characters")
    p=str((an/y)*100)+"%"
    print (p,"of characters are alpha numeric")

def question4():
    s=input("Enter a string boi: ")
    y=len(s)
    if s!="q":
        for a in range(0,y,1):
            z=s[a]
            if z.isupper():
                z=z.lower()
            elif z.islower():
                z=z.upper()
            print (z, end="")

def question5():
    s=input("Enter a string: ")
    x=int(input("Enter an integer: "))
    y=len(s)
    f=int(y)
    c=""
    for a in range(0,f,1):
        z=s[a]
        if z.isdigit():
            c=c+z
    if c=="":
        d=0
    else:
        d=int(c)
    h=d+x
    print (x,"+",d,"=",h)

def question6():
    a=input("Enter a string: ")
    b=input("Enter a string: ")
    if len(a)>len(b):
        l=a
        s=b
    else:
        l=b
        s=a
    print(s)
    print(l[0],"                 ",l[-1])
    print(" ",l[1],"             ",l[-2])
    print("   ",l[2],"         ",l[-3])

def question7():
    x=int(input("Input an integer: (smaller than 4000) "))
    r=""
    if x>3999:
        print ("Sorry, roman numerals go upto only 3999.")
    else:
        a=(x-(x%1000))//1000
        b=((x%1000)-(x%100))//100
        c=((x%100)-(x%10))//10
        d=x%10
        r=r+("M"*a)
        if b==9:
            r=r+"CM"
        elif b in (1,2,3):
            r=r+("C"*b)
        elif b==4:
            r=r+"CD"
        elif b in (5,6,7,8):
            r=r+"D"
            b=b-5
            if b in (1,2,3):
                r=r+("C"*b)
        if c==9:
            r=r+"XC"
        elif c in (1,2,3):
            r=r+("X"*c)
        elif c==4:
            r=r+"XL"
        elif c in (5,6,7,8):
            r=r+"L"
            c=c-5
            if c in (1,2,3):
                r=r+("X"*c)
        if d==9:
            r=r+"IX"
        elif d in (1,2,3):
            r=r+("I"*d)
        elif d==4:
            r=r+"IV"
        elif d in (5,6,7,8):
            r=r+"V"
            d=d-5
            if d in (1,2,3):
                r=r+("I"*c)
        print (r)
