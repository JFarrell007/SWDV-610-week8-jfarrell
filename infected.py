"""
Name: Jim Farrell
SWDV-610
Description: The Infected class uses randomness and various other weighted factors
to determin how many people in a given area will become infected. Each of the items
such as population density, living conditions, temperature and humidity are assigned
weight.  This weight is applied to the population to estimate the number of people that
will get the disease.
"""
from random import *

class Infected:

    def __init__(self, population, landArea):
        """constructor"""
        
        self.population = population
        self.landArea = landArea
        self.totalInfected = 0
        self.infectionProbability = 0
        self.temperature = 0
        self.humidity = 0
        self.livingConditions = 0 
        self.populationDensity = 0
    
    def createInfected(self):
        """this method uses the weights from the various factors to calculte the number of
        people in a given population will be infected.
        """
        self.calculateInfectionRatio()
        self.totalInfected = int(self.population * self.infectionProbability)
        return self.totalInfected
    
    def calculateInfectionRatio(self):
        """Method multiplies the various factors to get an estimate probability of infection"""
        self.infectionProbability = self.populationDensityFactor() * self.livingConditionsFactor() * self.temperatureFactor() * self.humidityFactor()
    
    def populationDensityFactor(self):
        """method to calculate population per square mile of area
        40000 people per sq mile is considered high.
        """
        density = self.population / self.landArea
        #1 or higher is considerd extremely dense
        return density / 40000
    
    def livingConditionsFactor(self):
        """Method that generates a random living conditions factor.
        The number is inversley porportinal to the quality of living
        higher is worse
        """
        self.livingConditions = random() + 0.01
        return self.livingConditions
    
    def temperatureFactor(self):
        """Method  that generates a temperature for the area.
        High temperatures increase growth rate of microbes
        """
        self.temperature = randrange(20, 110) / 110
        return self.temperature
    
    def humidityFactor(self):
        """Method  that generates a humidity for the area.
        High humidity increases growth rate of microbes
        """
        self.humidity = randrange(20, 100) / 100
        return self.humidity
    
    def printStats(self):
        print("This simulation has a population  {} in a {} square mile area".format(self.population, self.landArea))
        print("Various factors including population density, living conditions, humidity and temperature are used to determine probability of becoming infected")
        print("The probability of infection has a weight of {}".format(self.infectionProbability))
        print("This means that {} people will be infected from the {} person population".format(self.totalInfected,self.population))
        

