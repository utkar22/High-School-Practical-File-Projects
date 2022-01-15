"""This script determines the state of a given element at a given temperature in a given scale"""

from Connection import *
from conversions import celsius_to_kelvin as c, fahrenheit_to_kelvin as f, rankine_to_kelvin as r


#Basic function
def state(Z,t):
    m=points_dictionary[Z]["melting"]
    b=points_dictionary[Z]["boiling"]
    if t<m:
        return ("Solid")
    elif m<=t<=b:
        return ("Liquid")
    else:
        return ("Gas")


def state_1():
    method=input("Number/Name/Symbol>")
    if method=="Name":
        while True:
            name=input("Enter element name: ")
            #To make sure given input is valid
            if name in elements:
                Z=elements_dictionary[name]
                break
            else:
                print("Please enter a valid element")
    elif method=="Symbol":
        while True:
            symbol=input("Enter symbol: ")
            #To make sure given input is valid
            if symbol in symbols:
                Z=symbols_dictionary[symbol]
                break
    else:
        Z=int(input("Enter atomic number"))
    t_scale=input("Celsius/Kelvin/Fahrenheit/Rankine>")
    t_unscaled=int(input("Enter value of temperature: "))
    if t_scale=="Celsius":
        t=c(t_unscaled)
    elif t_scale=="Fahrenheit":
        t=f(t_unscaled)
    elif t_scale=="Rankine":
        t=r(t_unscaled)
    else:
        t=t_unscaled
    s=state(Z,t)
    print ("At the given temperature, the element is in",s,"state")

def room_temperature():
    method=input("Number/Name/Symbol>")
    if method=="Name":
        while True:
            name=input("Enter element name: ")
            #To make sure given input is valid
            if name in elements:
                Z=elements_dictionary[name]
                break
    elif method=="Symbol":
        while True:
            symbol=input("Enter symbol: ")
            #To make sure given input is valid
            if symbol in symbols:
                Z=symbols_dictionary[symbol]
                break
    else:
        Z=int(input("Enter atomic number"))
    s=state(Z,293)
    print ("At room temperature (293K), the element is in",s,"state")
          
              
