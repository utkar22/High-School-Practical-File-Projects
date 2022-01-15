"""This script can add elements to the mysql table"""

import mysql.connector
mydb=mysql.connector.connect(host="localhost",\
                             user="root",\
                             passwd="",\
                             database="test")

mycursor = mydb.cursor()

def add():
    atomic_number=int(input("Atomic Number>"))
    name=input("Name>")
    symbol=input("Symbol>")
    period_number=int(input("Period Number>"))
    group_number=int(input("Group Number>"))
    atomic_mass=float(input("Atomic Mass>"))
    melting_point=float(input("Melting Point"))
    boiling_point=float(input("Boiling Point"))
    command="INSERT INTO PERIODIC_TABLE values({},{},{},{},{},{},{},{})".format((atomic_number),(name),(symbol),(period_number),(group_number),(atomic_mass),(melting_point),(boiling_point))
    mycursor.execute(command)        
