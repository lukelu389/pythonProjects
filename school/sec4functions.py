import numpy as np
from matplotlib import pyplot as plt

class Function:
    roots = []
    fn = []

    def __init__(self, fn):
        self.fn = fn
        self.roots = self.findZeros()

    def findZeros(self): 
        return np.roots(self.fn)

    def displayGraph(self):
        x_nlimit = int(input("input the x negative limit of the graph"))
        x_plimit = int(input("input the x positive limit of the graph"))
        y_nlimit = int(input("input the y negative limit of the graph"))
        y_plimit = int(input("input the y positive limit of the graph"))

        x = []
        y = []

        for i in range(100):
            x.append(i)
            y.append(i)

            # Mention x and y limits to define their range
            plt.xlim(x_nlimit, x_plimit)
            plt.ylim(y_nlimit, y_plimit)

            # Plotting graph
            plt.plot(x, self.fn, color='green')
            plt.pause(0.01)

        plt.show()

    # def findExtrema(self):
    #
    #
    # def findVariation(self):
    #
    # def displaySign(self):
    #
    # def displayTable(self):
