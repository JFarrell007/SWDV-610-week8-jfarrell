"""
Name: Jim Farrell
SWDV-610
Description: The Simulator uses methods from the infected and transmission
classes to get the number of total infected and create the paths between the
infected.
"""
from infected import *
from transmission import *


class Simulator:

    def __init__(self, population, landArea):
        """constructor"""
        
        self.population = population #number of total people
        self.landArea = landArea#area in square miles
        self.totalInfected = 0
        self.calculateInfected()
        self.createInfectedPlot()
    
    def calculateInfected(self):
        """method instantiates an Infected object and gets the number of infected"""
        inf = Infected(self.population, self.landArea)
        self.totalInfected = inf.createInfected()
        inf.printStats()
        return self.totalInfected
    
    def createInfectedPlot(self):
        """method instantiates a Transmission object and creates the edgs/paths of how the
        disease spread.
        """
        plot = Transmission(self.totalInfected)
        plot.createInfectedPath()
        
    def getPopulation(self):
        return self.population
    



        