def question13():
    import matplotlib.pyplot as plt
    labels=["Science","Commerce","Humanities","Vocational","FMM"]
    ratio=360/100
    sizes=[29*ratio,30*ratio,21*ratio,13*ratio,7*ratio]
    colors=["goldenrod","gray","sienna","black","cyan"]
    plt.pie(sizes,labels=labels,colors=colors,startangle=140)
    plt.axis('equal')
    plt.show()

def question14():
    import matplotlib.pyplot as plt
    import numpy as np
    objects=["I","II","III","IV","V","VI","VII","VIII","IX","X"]
    y_pos=np.arange(len(objects))
    strength=[40,43,45,47,49,38,50,37,43,39]
    plt.barh(y_pos,strength,align="center",color="r")
    plt.yticks(y_pos,strength)
    plt.xlabel("Strength")
    plt.title("Class Strength")
    plt.show()

def question17():
    import matplotlib.pyplot as plt
    import numpy as np
    x=np.arange(0,20)
    y=(4*x)**(0.5)
    plt.plot(x,y)
    plt.show()
