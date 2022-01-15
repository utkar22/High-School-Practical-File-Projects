"""This script graphs

1) Celsius and Fahrenheit scale against Kelvin scale
2) Fahrenheit scale against Celsius scale

"""

import matplotlib.pyplot as plt
import numpy as np
import conversions

def kelvin_graph():
    kelvin=list(range(0,400))
    celsius=[]
    fahrenheit=[]
    for a in kelvin:
        celsius.append(conversions.kelvin_to_celsius(a))
        fahrenheit.append(conversions.kelvin_to_fahrenheit(a))
    plt.plot(kelvin,celsius,label="Celsius")
    plt.plot(kelvin,fahrenheit,label="Fahrenheit")
    plt.xlabel("Kelvin")
    plt.title("Kelvin vs Celsius and Fahrenheit")
    plt.grid()
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.legend()
    plt.show()

def celsius_vs_fahrenheit_graph():
    celsius=list(range(-150,150))
    fahrenheit=[]
    for a in celsius:
        fahrenheit.append(conversions.celsius_to_fahrenheit(a))
    plt.plot(celsius,fahrenheit)
    plt.xlabel("Celsius")
    plt.ylabel("Fahrenheit")
    plt.grid()
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()
    
