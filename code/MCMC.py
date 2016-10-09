# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:43:36 2016

@author: Ciwan
"""
from graph.node import Node
from graph.graph import Graph
import graph.path_finder as pf
from typing import Dict, List, Tuple, Set
import numpy as np
from warnings import warn
#from problem import Problem
    
class Problem:
    def __init__(self, nrBikers) -> None:
        self.nrNodes = 5
        self.nrBikers = nrBikers
        self.graph = Graph()
        self.orders = dict()
        for i in range(4):
            self.orders[i] = (Node(0.5*i, 0.5*i), Node(-0.5*i, -0.5*i))


class Sim_annSolver:
    REST = 0
    CUST = 1
    
    def __init__(self, data: Problem) -> None:
        """ Read in the problem data and store of use."""
        #Take the order dict and make a List of tuples. The first
        # index is typ type, "biker", "REST" or "CUST"
        self.nrNodes        = data.nrNodes
        self.nrBikers       = data.nrBikers
        self.graph          = data.graph
        self.costMatrix     = -1 * np.ones((data.nrNodes, data.nrNodes))
        self.nodeDicts      = List[Dict[int, Node]]
        self.nodeDicts      = [dict(), dict()]
        self.orders         = dict(data.orders)
        self.nrOrders       = 0
        print(self.orders)
        for o in range(len(self.orders)):
            self.nodeDicts[0][self.nrOrders] = self.orders[o][0]
            self.nodeDicts[1][self.nrOrders] = self.orders[o][1]
            self.nrOrders += 1
            
        self.solution       = Dict[int, List[Tuple[int, int]]] 
        self.solution       = dict()
        self.costOfRoutes   = Dict[int, float]
        self.searchOrder    = List[Tuple[int, int]] #bikers1, biker2
        self.searchOrder    = []
        for i in range(self.nrBikers):
            self.solution[i] = []
            for j in range(i+1, self.nrBikers):
                self.searchOrder.append((i, j))   
        return None
    
    def runSA() -> None:
        # Do initial heuristic solution, only vor variable number of bikers?
        
        #Initialize cooloing schedule parameters
        
        #lambda interchange + cost of move
        
        #apply acceptance criteria
        
        #update temperatures
        
        #check for stop
        
        return None
        
    def runLambdaDescent(self) -> None:
        # Do initial heuristic solution, only vor variable number of bikers?
        self.initializeSolution()
        # Now we have an initial self.solution
        # and en initial self.costOfRoutes
        
        #lambda interchange + cost of move
        neighbourhood = self.lambdaInterchange()
        # Now we have a 1-interchange neighbourhood, a set of possible solutions
        
        #Here we do an ordered search of these solutions
        #deltaCostOfSolution(): approximation of 
        #                 costOfSolution(S') - costOfSolution(S)
        
        #apply acceptance criteria
        
        #check for stop
        return None
    
    def initializeSolution(self) -> None:
        """Creates and initial feasible solution. Takes all the orders and 
        distributes them roughly equal among the bikers. Every biker goes 
        directly from the restaurant to the customer."""
        orders = list(range(self.nrOrders))
        b = 0
        while(len(orders) > 0):
            o = orders.pop()
            self.solution[b].append((self.REST, o))
            self.solution[b].append((self.CUST, o))
            b += 1
            b = b % self.nrBikers
        for b in range(self.nrBikers):
            self.costOfRoutes[b] = self.calcCostofRoute(self.solution[b])
        return None
            
    def calcCostofRoute(self, route: List[Tuple[int, int]]) -> float:
        """Calclulates the total time cost of a route. """
        cost = 0.0
        for i in range(len(route) - 1):
            node1 = self.nodeDicts[route[i][0]][route[i][1]]
            node2 = self.nodeDicts[route[i + 1][0]][route[i + 1][1]]
            cost += self.__getDistance(node1, node2)
        return cost
    
    def lambdaInterchange(self) -> List[Set[Tuple[int, int]]]:
        """WARNING: This function assumes R,C pairs.
        This function implements a 1-interchange mechanism for a carrying 
        capacity of 1 with 1 load per order.
        The function returns the a neighbourhood of solutions to the current 
        solution."""
        
        #neighbourhood = []
        neighbourhood2 = List[List[Tuple[int, int]]]
        neighbourhood2 = []
        for pair in self.searchOrder:
            biker1Route = list(self.solution[pair[0]])
            biker2Route = list(self.solution[pair[1]])
            len1        = len(biker1Route)
            stop1       = len1 + 1 if len1 == 0 else len1
            len2        = len(biker2Route)
            stop2       = len2 + 1 if len2 == 0 else len2
            #neighbour = dict(self.solution)
            neighbour2 = Set[Tuple[int, int]]
            neighbour2 = set()
            for inx1 in range(0, stop1, 2):
                for inx2 in range(0, stop2, 2):
                    if(len1 > 0):
#                        lists = self.__01operator(list(biker1Route), 
#                                                  list(biker2Route), inx1, inx2)
#                        neighbour[pair[0]] = list(lists[0])
#                        neighbour[pair[1]] = list(lists[1])
#                        neighbourhood.append(dict(neighbour))
                        neighbour2.add((inx1, -1))
                    if(len2 > 0):
#                        lists = self.__10operator(list(biker1Route), 
#                                                  list(biker2Route), inx1, inx2)
#                        neighbour[pair[0]] = list(lists[0])
#                        neighbour[pair[1]] = list(lists[1])
#                        neighbourhood.append(dict(neighbour))
                        neighbour2.add((-1, inx2))
                    if(len1 > 0 and len2 > 0):
#                        lists = self.__11operator(list(biker1Route), 
#                                                  list(biker2Route), inx1, inx2)
#                        neighbour[pair[0]] = list(lists[0])
#                        neighbour[pair[1]] = list(lists[1])
#                        neighbourhood.append(dict(neighbour))
                        neighbour2.add((inx1, inx2))
            neighbourhood2.append(neighbour2)
        return neighbourhood2
    
    """WARNING The following functions determine how orders are transfered between 
    bikers. These needs to be changed to account for capacity != 1 and 
    lambda > 1. """
    def __01operator(self, biker1Route: List, biker2Route: List,
                      inx1: int, inx2: int) -> Tuple[List]:
        r = biker1Route.pop(inx1)
        c = biker1Route.pop(inx1)
        biker2Route.insert(inx2, c)
        biker2Route.insert(inx2, r)
        return biker1Route, biker2Route
    
    def __10operator(self, biker1Route: List, biker2Route: List,
                      inx1: int, inx2: int) -> Tuple[List]:
        r = biker2Route.pop(inx2)
        c = biker2Route.pop(inx2)
        biker1Route.insert(inx1, c)
        biker1Route.insert(inx1, r)
        return biker1Route, biker2Route

    def __11operator(self, biker1Route: List, biker2Route: List,
                      inx1: int, inx2: int) -> Tuple[List]:
        r1 = biker1Route.pop(inx1)
        c1 = biker1Route.pop(inx1)
        r2 = biker2Route.pop(inx2)
        c2 = biker2Route.pop(inx2)        
        biker2Route.insert(inx2, c1)
        biker2Route.insert(inx2, r1)
        biker1Route.insert(inx1, c2)
        biker1Route.insert(inx1, r2)
        return biker1Route, biker2Route
    
    def getCostInsDelProcedure(self, bikerPair: Tuple[int, int], 
                               move: Tuple[int, int]) -> float:
        """WARNING this functions assumes R,C pairs """
        b1 = bikerPair[0]
        b2 = bikerPair[1]
        if(move[0] > -1 and move[1] > -1):
            routes = [list(self.solution[b1]), list(self.solution[b2])]
            r = [routes[0].pop(move[0]), routes[1].pop(move[1])]
            c = [routes[0].pop(move[0]), routes[1].pop(move[1])]
            lmin = np.inf
            cost = 0.0
            for n1 in range(2):
                n2 = (n1 + 1) % 2
                rest = r[n2]
                cust = c[n2]
                for i in range(0, len(routes[n1]), 2):
                    l = self.__calcL(routes[n1], i, rest, cust)
                    if l < lmin:
                        lmin = l
                cost += lmin
        else:
            if move[1] == -1:
                (von, nach) = (b1, b2)
                inx         = move[0]
            else:
                (von, nach) = (b2, b1)
                inx         = move[1]
            routeVon    = list(self.solution[von])
            routeNach   = list(self.solution[nach])
            r = routeVon.pop(inx)
            c = routeVon.pop(inx)
            deletionCost = -1 * self.__calcL(routeVon, inx, r, c)
            lmin = np.inf
            for i in range(0, len(routeNach), 2):
                l = self.__calcL(routeNach, i, r, c)
                if l < lmin:
                    lmin = l            
            cost = deletionCost + lmin

               
        return cost
    
    def __calcL(self, route: List[Tuple[int, int]], inx: int, 
                rest: Tuple[int, int], cust: Tuple[int, int]) -> float:
        l = 0.0
        if inx > 1:
            order1 = self.route[inx - 1]
            if order1[0] != 1:
                warn("Some thing is wrong! Trying to insert after R.")
            l += self.__getDistance(self.nodeDicts[order1[0]][order1[1]],
                                    self.nodeDicts[rest[0]][rest[1]])
        l += self.__getDistance(self.nodeDicts[rest[0]][rest[1]],
                                self.nodeDicts[cust[0]][cust[1]])
        if inx < len(route) - 1:
            order2 = self.route[inx]
            if order2[0] != 0:
                warn("Some thing is wrong! Trying to insert before C.")
            l += self.__getDistance(self.nodeDicts[cust[0]][cust[1]],
                                    self.nodeDicts[order2[0]][order2[1]])
        if inx > 1 and inx < len(route) - 1:
            l -= self.__getDistance(self.nodeDicts[order1[0]][order1[1]], 
                                    self.nodeDicts[order2[0]][order2[1]])
        return l
        
    def getDeltaCostSoulutionA(self, 
                               newSolution: Dict[int, List[Tuple[int, int]]]):
        deltaCost = 0.0
        for b in range(self.nrBikers):
            deltaCost += self.getCostInsDelProcedure(newSolution[b], b, )
        
    def __getDistance(self, start: Node, goal: Node) -> float:
        # Check matrix
        # Otherwise calc distance and add to matrix
        distance = 0.0
        if(self.costMatrix[start.getID(), goal.getID()] > -1):
            distance = self.costMatrix[start.getID(), goal.getID()]
        else:
            distance = pf.a_star_search(self.graph, start, goal)
            self.costMatrix[start.getID(), goal.getID()] = distance
            self.costMatrix[goal.getID(), start.getID()] = distance
        return distance
        
     
if __name__ == "__main__":
    data = Problem(3)
    simulator = Sim_annSolver(data)
 #   simulator.initializeSolution()
    simulator.solution[0] = [(0,0), (1,0), (0,1), (1,1)]
    simulator.solution[1] = [(0,2), (1,2)]
    simulator.solution[2] = [(0,3), (1,3)]
    neighbourhood = simulator.lambdaInterchange()
    simulator.getCostInsDelProcedure((0, 1), (0, 0))
#    for o in neighbourhood:
#        print(o)