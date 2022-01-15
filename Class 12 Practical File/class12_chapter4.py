f=open("poem.txt","r")
l=f.read()
f.close()

def question15():
    l2=l.split()
    to=l2.count("to")
    the=l2.count("the")
    print ("to:",to,"the:",the)

def question16():
    upper=0
    for a in l:
        if a.isupper()==True:
            upper+=1
    return (upper)

def question17():
    f1=input("Name of original file: ")
    f2=input("Name of copying file: ")
    f1+=".txt"
    f2+=".txt"
    f=open(f1,"r")
    l=f.read()
    f.close()
    f=open(f2,"w")
    f.write(l)
    f.close()
    
