def q1(election):
    l=list()
    l1=list()
    l2=list()
    for a in election:
        l.append([a,election[a]])
    for i in range (1,len(l)):
        for j in range(i,0,-1):
            if l[j][1]>l[j-1][1]:
                temp=l[j-1]
                l[j-1]=l[j]
                l[j]=temp
            else:
                break
    for b in l:
        l1.append(b[0])
        l2.append(b[1])
    for c in range(0,len(l1)):
        print ("name:",l1[c],"votes recieved:",l2[c])
    

def q2(l):
    for a in range(0,len(l)):
        l[a][0]=l[a][0].split() #l[a][0]=l[a][0][(len(l[a][0]))-1]
    for i in range (1,len(l)):
        for j in range(i,0,-1):
            if l[j][0][-1]<l[j-1][0][-1]:
                temp=l[j-1]
                l[j-1]=l[j]
                l[j]=temp
            else:
                break
    for b in range(0,len(l)):
        c=""
        for d in l[b][0]:
            c+=d+" "
        c=c[0:-1]
        l[b][0]=c
    print (l) 
    
def q3(data_list):
    for k in range(1,len(data_list)):
        t=data_list[k]
        ptr=k-1
        while (ptr>=0) and (data_list[ptr]%10)>(t%10):
            data_list[ptr+1]=data_list[ptr]
            ptr=ptr-1
        else:
            data_list[ptr+1]=t
    print (data_list)

def q4(data_list):
    for k in range(1,len(data_list)):
        t=data_list[k]
        ptr=k-1
        while (ptr>=0) and len(data_list[ptr])>len(t):
            data_list[ptr+1]=data_list[ptr]
            ptr=ptr-1
        else:
            data_list[ptr+1]=t
    print (data_list)

def q5(a):
    for i in range(len(a)):
        for j in range(0,len(a)-i-1,1):
            if a[j][2]>a[j+1][2]:
                a[j],a[j+1]=a[j+1],a[j]
    print ("After sorting:",a)
    
