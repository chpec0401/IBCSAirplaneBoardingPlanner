import matplotlib.pyplot as plt
from py4j.java_gateway import JavaGateway, GatewayParameters
import jpype
import os
import numpy as np
import json
class Genetic():
    data=0
    passengers=0
    aircraft=0
    def __init__(self, num, type):
        self.passengers = num
        self.airCraft = type
        jarpath = os.path.join(os.path.abspath('.'), r'C:\Users\Eric Chang\PycharmProjects\IA\IA.jar')
        dependency = os.path.join(os.path.abspath('.'), 'C:\\Users\\Eric Chang\\PycharmProjects\\IA\\dependencies')

        jvmPath = 'C:\Program Files\Java\jdk-18.0.2.1\\bin\server\jvm.dll'

        jpype.startJVM(jvmPath, "-ea", "-Djava.class.path=%s" % jarpath)
        JClass = jpype.JClass('geneticRef.narrow')
        thing = JClass(num, type)
        jpype.shutdownJVM()
        data=np.zeros((32,7))
        f = open("C:\\Users\\Eric Chang\\PycharmProjects\\IA\\problemname.txt", "r")
        for i in range (0,32):
            arr=f.readline().split(',')
            for j in range(0,7):
                data[i][j]=int(arr[j])
        self.data=data
        f.readline()
        a=f.readline()
        a=float(a.replace("\n",""))
        #print (a)
        f.close()



    def generate(self):
        plt.plot()
        plt.imshow(self.data, cmap='summer', interpolation='nearest')
        plt.show()
        return self.data