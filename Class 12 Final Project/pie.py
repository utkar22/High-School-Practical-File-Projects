"""This script plots a pie chart of the ratio of elements in solid, liquid and gas state at room temperature"""

from states import state
from Connection import no_of_elements as Z
import matplotlib.pyplot as plt

l=[]
for a in range(1,Z+1):
    l.append(state(a,298))

solid=l.count("Solid")
liquid=l.count("Liquid")
gas=l.count("Gas")

print ("At room temperature")

#Data to plot
labels=["Solid","Liquid","Gas"]
sizes=[solid*360/Z,liquid*360/Z,gas*360/Z]
colors=["red","blue","green"]

#Plot
plt.pie(sizes,labels=labels,colors=colors,startangle=140)
plt.axis('equal')
plt.show()
