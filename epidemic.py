"""
Name: Jim Farrell
SWDV-610
Description: The Epidemic class starts the simulation and uses networkx and
matplotlib to disply the graphic model of the spread of a disease.
If will open two windows.  Figure 1 represents all infected and the connections between
the infected and path from first infected to last infected.
Figure 2 represents the path from first infected to last infected and includes labels.
"""
import networkx as nx
import matplotlib.pyplot as plt
from simulator import *
import time

class Epidemic:
    def __init__(self):
        """constructor creates networkx graphs"""
        self.infectedGraph = nx.read_edgelist('infected.edgelist', create_using=nx.Graph(), nodetype=str)
        self.firstToLastGraph = nx.Graph()
        
    def buildNodeColorMap(self, graph):
        """method to generate colors for nodes return color_map with a color for each node"""
        color_map = []
        #get the last node in the graph
        lastNode = nx.number_of_nodes(graph)
        for i in range(lastNode):
            if i == 0:
                #First infected will be red
                color_map.append('red')
            elif i == lastNode - 1:
                #last infected will be blue
                color_map.append('blue')
            else:
                #all other infected will be green
                color_map.append('green')
        return color_map
    
    def buildEdgeColorMap(self):
        """method to create red line to show edge path from first infected to last infected.
        returns a list of colors to be assigend to the edges
        """
        edge_color_list = []
        lastNode = nx.number_of_nodes(self.infectedGraph)
        #Get the shortest path from first infected to last infected
        path = (nx.shortest_path(self.infectedGraph, source = "Infected1", target = "Infected" + str(lastNode)))
        #Initially set all to black
        for edge in self.infectedGraph.edges():
            self.infectedGraph[edge[0]][edge[1]]['color'] = 'black'
        #Set the edges on the shortest path to red
        for i in range(len(path) -1 ):
            self.infectedGraph[path[i]][path[i+1]]['color'] = 'red'
        #apped the colors to the edge_color_list to create a one to one mapping of colors to edges    
        for edge in self.infectedGraph.edges():
            edge_color_list.append(self.infectedGraph[edge[0]][edge[1]]['color'])

        return edge_color_list
        
        
        
    def buildGraphs(self):
        """method to create and draw the graphs"""
 
        lastNode = nx.number_of_nodes(self.infectedGraph)
        #title of all infected window
        plt.figure(1).canvas.set_window_title("Infected")
        #Text in window
        plt.title("Total Infected {}. Path indicates travel of first infected RED to last infected BLUE".format(str(lastNode)) )
        #draw graph of all infected with nodes, paths incorporating colors
        nx.draw(self.infectedGraph,node_color = self.buildNodeColorMap(self.infectedGraph), edge_color = self.buildEdgeColorMap(), node_size=30)
        #get the path from the first infected to last infected
        firstToLast = (nx.shortest_path(self.infectedGraph, source = "Infected1", target = "Infected" + str(lastNode)))
        #Add the nodes from shortest path to second graph
        self.firstToLastGraph.add_nodes_from(firstToLast)

        #add the connecting edges to the second graph
        for i in range(len(firstToLast) -1 ):
            self.firstToLastGraph.add_edge(firstToLast[i],firstToLast[i+1])
        #Title of second window
        plt.figure(2).canvas.set_window_title('First to Last')
        #Text in window
        plt.title("Path from first infected RED to last infected BLUE")
        #draw the second graph with colors
        nx.draw(self.firstToLastGraph, node_color=self.buildNodeColorMap(self.firstToLastGraph),node_size=30, with_labels = True)
        #Finally show both of the windows
        plt.show()

def runTest():
    """Method to run and display the simulation"""
    #100000 people in 100 square miles
    sim = Simulator(100000, 100)
    #time.sleep(10)

    
    epidemic = Epidemic()
    epidemic.buildGraphs()
    
runTest()

