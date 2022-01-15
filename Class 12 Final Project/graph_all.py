"""This script plots graphs for melting points and boiling points of all elements"""

from Connection import no_of_elements,melting,boiling
import matplotlib.pyplot as plt

Z=list(range(1,no_of_elements+1))

def graph_melting():
    plt.plot(Z,melting,label="Melting Point")
    plt.xlabel("Atomic Number")
    plt.ylabel("Melting Point (in Kelvin)")
    plt.grid()
    plt.axhline(y=0, color='k')  #x axis
    plt.axvline(x=0, color='k')  #y axis
    plt.axhline(y=298, color='g', label="Room Temperature")
    plt.legend()
    plt.show()

def graph_boiling():
    plt.plot(Z,boiling,label="Boiling Point")
    plt.xlabel("Atomic Number")
    plt.ylabel("Boiling Point (in Kelvin)")
    plt.grid()
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.axhline(y=298, color='g', label="Room Temperature")
    plt.legend()
    plt.show()

def graph_both():
    plt.plot(Z,melting,label="Melting Point")
    plt.plot(Z,boiling,label="Boiling Point")
    plt.xlabel("Atomic Number")
    plt.ylabel("Temperature (in Kelvin)")
    plt.grid()
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.axhline(y=298, color='g', label="Room Temperature")
    plt.legend()
    plt.show()
