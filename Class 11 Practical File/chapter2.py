def question6():
    pi=22.0/7.0
    z=int(input("Radius of circle? "))
    a=pi*z*z
    c=2*pi*z
    print ('The area of the circle is',a,'units and the circumfrence of the circle is',c)

def question7():
    a=int(input("What was your percentage in subject 1? "))
    b=int(input("What was your percentage in subject 2? "))
    c=int(input("What was your percentage in subject 3? "))
    d=int(input("What was your percentage in subject 4? "))
    e=int(input("What was your percentage in subject 5? "))
    avg=(a+b+c+d+e)/5
    print(avg)


def question10(b,h):
    area=b*h*0.5
    print ("The area of the triangle is",area)

def question11():
    p=int(input("What is the principal amount? "))
    r=int(input("What is the rate of interest? "))
    t=int(input("How many years? "))
    si=p+((p*r*t)/100)
    ci=p*((1+(r/100))**t)
    print ("The amount after",t,"years is",si,"if simple interest annually, or",ci,"if compunded annually")

def question13():
    name=input("Name: ")
    grade=int(input("Class: "))
    age=int(input("Age: "))
    print ("Name:",name,end="   ")
    print ("Grade:",grade,end="   ")
    print ("Age:",age)
    print ("""
""")
    print ("Name:",name)
    print ("Grade:",grade)
    print ("Age:",age)

def question14():
    x=int(input ("Enter a single digit (1 to 7): "))
    a=str(x)+str(x+1)+str(x+2)
    print (a)

def question15(a,b,c):
    aa=a
    bb=b
    a=a+bb
    b=bb+c
    print(a,b,c)
    
