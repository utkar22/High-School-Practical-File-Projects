"""This script pulls data from mysql database and converts them into python objects needed in other scripts"""

import mysql.connector
mydb=mysql.connector.connect(host="localhost",\
                             user="root",\
                             passwd="",\
                             database="test")

mycursor = mydb.cursor()

#For the full dictionary
mycursor.execute("SELECT * FROM periodic_table")
x=mycursor.fetchall()

dictionary={}


for a in x:
    dictionary[a[0]]={"Name":a[1],"Symbol":a[2],"Period Number":a[3],"Group Number":a[4],"Atomic Mass":a[5],"Melting Point":a[6],"Boiling Point":a[7]}


#For a list of Element Names and Symbols

mycursor.execute("SELECT name,symbol FROM periodic_table")
elements=[]
symbols=[]
b=mycursor.fetchall()
for c in b:
    elements.append(c[0])
    symbols.append(c[1])

elements_dictionary={}
symbols_dictionary={}

for d in range(1,len(elements)+1):
    elements_dictionary[elements[d-1]]=d
    symbols_dictionary[symbols[d-1]]=d

no_of_elements=len(elements) #Number of Elements present

#For melting and boiling points

points_dictionary={}
melting=[]
boiling=[]

mycursor.execute("SELECT Atomic_Number,melting_point,boiling_point from periodic_table")
x=mycursor.fetchall()
for e in x:
    points_dictionary[e[0]]={"melting":e[1],"boiling":e[2]}
    melting.append(e[1])
    boiling.append(e[2])

#For atomic mass

mycursor.execute("SELECT Atomic_Number,atomic_mass from periodic_table")
x=mycursor.fetchall()

mass_dictionary={}
mass=[]
mass_ratio=[]

for f in x:
    mass_dictionary[f[0]]=f[1]
    mass.append(f[1])
    mass_ratio.append(f[1]/f[0])

del (a,b,c,d,e,f,x)
