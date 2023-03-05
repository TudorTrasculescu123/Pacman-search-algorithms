# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from node import Node


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def makeDfsOrBfs(problem: SearchProblem, myCollection, bol):
    from game import Directions
    node = Node(problem.getStartState(), None, Directions.SOUTH)
    statesVisited = []
    if bol == True:
        statesVisited.append(node.getState())
    myCollection.push(node)
    while not myCollection.isEmpty():
        node = myCollection.pop()
        currentState = node.getState()
        if problem.isGoalState(currentState):
            break
        for successor, action, cost in problem.getSuccessors(currentState):
            if successor not in statesVisited:
                if bol == True:
                    statesVisited.append(successor)
                myCollection.push(Node(successor, node, action))
        if bol == False:
            statesVisited.append(currentState)
    actionList = []
    while node.getParent() != None:
        actionList.append(node.getAction())
        node = node.getParent()
    actionList.reverse()
    ##print("The final steps: ", [e for e in actionList])
    return actionList

def depthLimitedSearch(problem: SearchProblem, maxDepth):
    from game import Directions
    node = Node(problem.getStartState(), None, Directions.SOUTH)
    stack = util.Stack()
    statesVisited = []
    solutionFound = False
    stack.push(node)
    while not stack.isEmpty():
        node = stack.pop()
        currentState = node.getState()
        if problem.isGoalState(currentState):
            solutionFound = True
            break
        if node.depth < maxDepth:
            for successor, action, cost in problem.getSuccessors(currentState):
                if successor not in statesVisited:
                    stack.push(Node(successor, node, action, 0, node.depth + 1))
        statesVisited.append(currentState)
    if not solutionFound:
        return False
    actionList = []
    while node.getParent() != None:
        actionList.append(node.getAction())
        node = node.getParent()
    actionList.reverse()
    return actionList


def iterativeDeepeningSearch(problem: SearchProblem, depthRange):
    for i in range(depthRange + 1):
        possibleSolution = depthLimitedSearch(problem, i)
        if possibleSolution != False:
            print("The solution was found with depth: " + str(i) + ":" )
            print(possibleSolution)
            return possibleSolution
    return False


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    """
    #return iterativeDeepeningSearch(problem, 250)
    return makeDfsOrBfs(problem, util.Stack(), False)

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    return makeDfsOrBfs(problem, util.Queue(), True)


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    node = Node(problem.getStartState(), None, Directions.SOUTH, 0)
    priorityQueue = util.PriorityQueue()
    statesVisited = []
    priorityQueue.push(node, 0)
    while not priorityQueue.isEmpty():
        node = priorityQueue.pop()
        currentState = node.getState()
        if problem.isGoalState(currentState):
            break
        costToThisPoint = node.getCost()
        if currentState not in statesVisited:
            for successor, action, cost in problem.getSuccessors(currentState):
                if successor not in statesVisited:
                    priorityQueue.push(Node (successor, node, action, cost + costToThisPoint), cost + costToThisPoint)
        statesVisited.append(currentState)
    actionList = []
    while node.getParent() != None:
        actionList.append(node.getAction())
        node = node.getParent()
    actionList.reverse()
    print("The final steps: ", [e for e in actionList])
    return actionList


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    node = Node(problem.getStartState(), None, Directions.SOUTH, 0)
    priorityQueue = util.PriorityQueue()
    statesVisited = []
    priorityQueue.push(node, 0)
    while not priorityQueue.isEmpty():
        node = priorityQueue.pop()
        currentState = node.getState()
        if problem.isGoalState(currentState):
            break
        costToThisPoint = node.getCost()
        if currentState not in statesVisited:
            for successor, action, cost in problem.getSuccessors(currentState):
                if successor not in statesVisited:
                    priorityQueue.push(Node (successor, node, action, cost + costToThisPoint), cost + costToThisPoint + heuristic(successor, problem))
        statesVisited.append(currentState)
    actionList = []
    while node.getParent() != None:
        actionList.append(node.getAction())
        node = node.getParent()
    actionList.reverse()
    ##print("The final steps: ", [e for e in actionList])
    return actionList


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
