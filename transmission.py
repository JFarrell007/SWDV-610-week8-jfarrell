"""
Name: Jim Farrell
SWDV-610
Description: The Transmission class uses randomness and recursion to 
create edges/connections other infected.  This creates a path from Infected1
to the last Infected in the simulation.
"""
from random import *
import networkx as nx

class Transmission:
    
    def __init__(self,infected):
        self.infected = infected
        self.infectedCount = 0
        self.increment = self.infected / 4
        
    
    def createInfectedPath(self):
        """method to write out lines to a file containing the
        patient names Infected1 to InfectedN.  Calls createEdges to create
        random edges to other Infected
        """
        #open the infected.edgelist file for writing
        file = open('infected.edgelist','w+')
        #Each increment is roughy 1/4th the total of infected.
        #call createEdges with a segment of the total infected for better distribution
        self.createEdges("Infected1", file, self.increment)
        self.createEdges("Infected1", file, self.increment * 2)
        self.createEdges("Infected1", file, self.increment * 3)
        self.createEdges("Infected1", file, self.infected)
        #close the file
        file.close()
        
    
    def createEdges(self, startName, file, increment):
        """method to create edges or connections between the infected.  Uses
        some randomness and recursion to complete this task.  Writes results
        to a file.
        """
        #keep going until the increment of infected is done
        while self.infectedCount < increment:
            self.infectedCount += 1
            #print(startName, "Infected" + str(self.infectedCount))
            #write the edge connection to the file
            line = (startName + " Infected" + str(self.infectedCount) + "\n")
            file.write(line)
            #add random number of infected edges to startName.  
            for i in range(randrange(1,5)):
                #self.infectedCount += 1
                if self.infectedCount < self.infected:
                    self.infectedCount += 1
                    #print(startName, "Infected" + str(self.infectedCount))
                    line = (startName + " Infected" + str(self.infectedCount) + "\n")
                    #write to the edgelist
                    file.write(line)
            #set the new startName to another random infected person     
            startName = "Infected" + str(randrange(1, self.infectedCount))
            #Use recursion to go through the increment of infected people
            self.createEdges(startName, file, increment)
        
#trans = Transmission(775)
#trans.createInfectedPath()
        