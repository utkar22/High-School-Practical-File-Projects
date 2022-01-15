def question1():
    d={}
    n=int(input("How many teams? "))
    for a in range(0,n):
        team=input("What is the name of the team? ")
        w=int(input("How many match won? "))
        l=int(input("How many match lost? "))
        d[team]=(w,l)
    question1a(d)
    question1b(d)
    question1c(d)

def question1a(d):
    while True:
        t=input("Which team?")
        if t=="exit":
            break
        w,l=d[t]
        p=(w/(w+l))*100
        print ("The win percentage of",t,"is",p,"%")

def question1b(d):
    list=[]
    for t in d:
        w,l=d[t]
        list.append(w)
    print (list)

def question1c(d):
    list=[]
    for t in d:
        w,l=d[t]
        if w>l:
            list.append(t)
    print (list)

def question2():
    d={}
    while True:
        name=input("Enter product name: ")
        if name=="exit":
            break
        price=int(input("What is the price? "))
        d[name]=price
    print ()
    while True:
        x=input("Which product do you want to see? ")
        if x=="exit":
            break
        print("The price is:",d.get(x,"Product is not in directory"))
        
days={"January":31,"February":28,"March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"September":30,"October":31,"November":30,"December":31}

def question3a(month):
    print ("There are",days[month],"days in",month)

def question3b():
    month=list(days.keys())
    month.sort()
    print (month)

def question3c():
    for a in days:
        if days[a]==31:
            print (a)

def question3d():
    a=[]
    for x in days:
        a.append([x,days[x]])
    for i in range(0,len(a)):
        t=0
        for j in range(0,len(a)-i-1):
            if a[j][1]>a[j+1][1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                t=1
        if t==0:
            break
    for y in a:
        print (y[0],":",y[1])

def question5():
    x={"k1":"v1","k2":"v2","k3":"v3"}
    k=tuple(x.keys())
    v=tuple(x.values())
    inverted_x=dict(zip(v,k))
    print (inverted_x)

def question6(d1,d2):
    l=[]
    for a in d1:
        if a in d2:
            l.append(a)
    print (l)

def question7(d):
    n=0
    v=list(d.values())
    for a in v:
        b=v.count(a)
        if b>1:
            n=b
    if n==0:
        n="No"
    print (n,"keys have same value")
    
    
        
