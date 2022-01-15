"""This script performs conversion between different temperature scales"""

def celsius_to_kelvin(c):
    k=c+273.15
    return (k)

def kelvin_to_celsius(k):
    c=k-273.15
    return (c)

def celsius_to_fahrenheit(c):
    f=(c*9/5)+32
    return (f)

def fahrenheit_to_celsius(f):
    c=(f-32)*5/9
    return (c)

def kelvin_to_fahrenheit(k):
    c=kelvin_to_celsius(k)
    f=celsius_to_fahrenheit(c)
    return (f)

def fahrenheit_to_kelvin(f):
    c=fahrenheit_to_celsius(f)
    k=celsius_to_kelvin(c)
    return (k)

def kelvin_to_rankine(k):
    r=k*9/5
    return (r)

def rankine_to_kelvin(r):
    k=r*5/9
    return (k)

def celsius_to_rankine(c):
    k=celsius_to_kelvin(c)
    r=kelvin_to_rankine(k)
    return (r)

def rankine_to_celsius(r):
    k=rankine_to_kelvin(r)
    c=kelvin_to_celsius(k)
    return (c)

def fahrenheit_to_rankine(f):
    r=f+459.67
    return (r)

def rankine_to_fahrenheit(r):
    f=r-459.67
    return (f)
