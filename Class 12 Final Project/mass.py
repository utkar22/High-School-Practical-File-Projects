"""This script performs two functions

1)It pulls out Atomic Mass for desired Atomic Number, Element or Symbol
2)It plots a graph of Atomic Masses against Atomic Number
and a graph of ratio of Atomic Mass to Atomic Number against Atomic Number

"""

from Connection import no_of_elements,mass,mass_ratio,mass_dictionary,elements_dictionary,symbols_dictionary
import matplotlib.pyplot as plt

#For pulling out Atomic Mass

def mass_from_Z(Z):
    m=mass_dictionary[Z]
    return (m)

def mass_from_name(name):
    Z=elements_dictionary[name]
    return (mass[Z-1])

def mass_from_symbol(symbol):
    Z=symbols_dictionary[symbol]
    return (mass[Z-1])

#For graphs
Z=list(range(1,no_of_elements+1))

def mass_graph():
    plt.plot(Z,mass,label="Atomic Mass")
    plt.xlabel("Atomic Number")
    plt.ylabel("Atomic Mass (in amu)")
    plt.grid()
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()

def mass_ratio_graph():
    plt.plot(Z,mass_ratio)
    plt.xlabel("Atomic Number")
    plt.ylabel("Atomic Mass/Atomic Number")
    plt.grid()
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()
