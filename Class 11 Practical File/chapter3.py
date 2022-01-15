def question1():
    p=int(input("What is the principal amount? "))
    r=int(input("What is the rate of interest? "))
    t=int(input("How many years? "))
    si=((p*r*t)/100)
    print ("The simple interest after",t,"years is",si)

def question2():
    t1=int(input("What is the temperature on Monday? (In Celsius) "))
    t2=int(input("What is the temperature on Tuesday? (In Celsius) "))
    t3=int(input("What is the temperature on Wednesday? (In Celsius) "))
    t4=int(input("What is the temperature on Thursday? (In Celsius) "))
    t5=int(input("What is the temperature on Friday? (In Celsius) "))
    t6=int(input("What is the temperature on Saturday? (In Celsius) "))
    t7=int(input("What is the temperature on Sunday? (In Celsius) "))
    t=(t1+t2+t3+t4+t5+t6+t7)/7
    print ("The average temperature of the week is",t,"degrees Celsius")

def question3():
    pi=22/7
    x=int(input("Enter x "))
    y=int(input("Enter y "))
    z=int(input("Enter z "))
    a=(4*(x**4))+(3*(y**3))+(9*z)+(6*pi)
    print (a)

def question4(sec):
    s=sec%60
    m=sec//60
    print (m,"minutes",s,"seconds")

def question5():
    x=int(input("Enter hour between 1 and 12 : "))
    y=int(input("How many hours ahead : "))
    t=x+y
    t=t%12
    print ("Time at that time would be :",t,"O\'clock")

def question6():
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

def question7(a,b):
    if a%b==0:
        print ("Fully divisible")
    else:
        print ("Not fully divisible")

def question8(a):
    b=((a%10)*10)+(a//10)
    print(b)

def question10():
    d=int(input("Day of the month: "))
    m=int(input("Month: "))
    dy=((m-1)*30)+d
    print ("Day of the year:",dy)
    
    
    
