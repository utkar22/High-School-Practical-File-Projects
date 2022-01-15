def question7():
    l=[]
    while True:
        x=input("Enter a name>")
        if x=="":
            break
        l.append(x)
    print (l)

#Question 11

books=["Pride and Prejudice","The Great Gatsby","To Kill a Mockingbird","Brave New World","A Tale of Two Cities","Great Expectations","Oliver Twist","The Adventures of Tom Sawyer","Adventures of Huckleberry Finn"]

def add(book):
    books.append(book)

def delete():
    books.pop(0)
