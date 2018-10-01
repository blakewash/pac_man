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
    return [s, s, w, s, w, w, s, w]


class Node:
    """
    We recommend that you implement a Node class for bookkeeping.
    Note that you should override the  __hash__ and __eq__ internal methods.
    """

    def __init__(self, l, a, t):
        self.track = []
        self.actions = []
        self.total = 0
        i = 0
        for x in l:
            self.track.insert(i,x)
            i += 1
        i = 0
        for y in a:
            self.actions.insert(i,y)
            i += 1
        self.total = t


    def add(self, item):
        self.track.insert(len(self.track), item[0])
        self.actions.insert(len(self.actions), item[1])
        self.minus = item[2]
        self.total += self.minus

    def pop(self):
        self.track.pop()
        self.actions.pop()
        self.total -= self.minus
    
    def get_state(self):
        return self.track[len(self.track) - 1]


    def __hash__(self):
        '''YOUR CODE HERE'''
        return None

    def __eq__(self, other):
        '''YOUR CODE HERE'''
        return None

    def trace(self):
        """
        Return the list of actions by tracing through
        the chain of parent member variables.

        Recommended but not required to have.
        """
        
        return self.actions


def depthFirstTreeSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    problem.getStartState(): returns a pair (tuple of size 2) that represents
    the coordinate of where the pacman starts

    problem.isGoalState((x, y)): returns a boolean True/False based on whether
    the coordinate (x, y) is a goal state.

    problem.getSuccessors((x, y)): given a position (x, y), returns a list of
    triples (list of tuples, with each tuple being size 3) of the successor
    positions of pacman.
    The tuple consists of position, action required to get to it, and the step
    cost i.e. ((35,2), 'North', 1).

    Remember to use the data structures in util.py: Stack, Queue, or
    PriorityQueue

    Remember to process the list of successors as a batch for the current state.

    For the search functions, you are required to return a list of actions
    (that is, a list of strings such as ['North', 'North', 'West'])
    """
    '''YOUR CODE HERE'''

    l = []
    c = problem.getStartState()
    l.insert(0,c)
    n = Node(l, [], 0)
    fringe = util.Stack()

    while problem.isGoalState(c) != True:
        l = problem.getSuccessors(c)
        for x in l:
            n.add(x)
            fringe.push(Node(n.track, n.actions, n.total))
            n.pop()
        if len(fringe.list) == 0:
            break
        n = fringe.list.pop()
        c = n.get_state()

    if problem.isGoalState(c):
        print("Goal Reached!")
    else:
        print("Goal not found.") 

    return n.trace()


def breadthFirstTreeSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    '''YOUR CODE HERE'''

    l = []
    c = problem.getStartState()
    l.insert(0,c)
    n = Node(l, [] , 0)
    fringe = util.Queue()

    while problem.isGoalState(c) != True:
        l = problem.getSuccessors(c)
        for x in l:
            n.add(x)
            fringe.push(Node(n.track, n.actions, n.total))
            n.pop()
        if len(fringe.list) == 0:
            break
        n = fringe.list.pop()
        c = n.get_state()

    if problem.isGoalState(c):
        print("Goal Reached!")
    else:
        print("Goal not found.") 

    return n.trace()


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Use a graph search here.
    """
    l = []
    closed = []
    c = problem.getStartState()
    l.insert(0,c)
    closed.insert(0,c)
    n = Node(l, [], 0)
    fringe = util.Stack()

    while problem.isGoalState(c) != True:
        l = problem.getSuccessors(c)
        for x in l:
            n.add(x)
            if n.get_state() not in closed:
                fringe.push(Node(n.track, n.actions, n.total))
                closed.insert(0,n.get_state())
            n.pop()
        if len(fringe.list) == 0:
            break
        n = fringe.list.pop()
        c = n.get_state()
        closed.insert(0,c)

    if problem.isGoalState(c):
        print("Goal Reached!")
    else:
        print("Goal not found.") 

    return n.trace()


def breadthFirstSearch(problem):
    l = []
    closed = []
    c = problem.getStartState()
    l.insert(0,c)
    closed.insert(0,c)
    n = Node(l, [], 0)
    fringe = util.Queue()

    while problem.isGoalState(c) != True:
        l = problem.getSuccessors(c)
        for x in l:
            n.add(x)
            if n.get_state() not in closed:
                fringe.push(Node(n.track, n.actions, n.total))
                closed.insert(0,n.get_state())
            n.pop()
        if len(fringe.list) == 0:
            break
        n = fringe.list.pop()
        c = n.get_state()
        closed.insert(0,c)

    if problem.isGoalState(c):
        print("Goal Reached!")
    else:
        print("Goal not found.") 

    return n.trace()


def iterativeDeepeningSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Use your own max_depth variable (you will be tuning this).
    Write this function iteratively, not recursively.
    """
    '''YOUR CODE HERE'''
    limit = 1000
    c = problem.getStartState()
    if problem.isGoalState(c):
        print("Goal Reached!")
        return []

    for i in range (0,limit):
        l = []
        closed = []
        c = problem.getStartState()
        l.insert(0,c)
        closed.insert(0,c)
        n = Node(l, [], 0)
        fringe = util.Stack()
        for j in range (0,i):
            if problem.isGoalState(c):
                print("Goal Reached!")
                return n.trace()
            l = problem.getSuccessors(c)
            for x in l:
                n.add(x)
                if n.get_state() not in closed:
                    fringe.push(Node(n.track, n.actions, n.total))
                    closed.insert(0,n.get_state())
                n.pop()
            if len(fringe.list) == 0:
                "failed"
                return n.trace()
            n = fringe.list.pop()
            c = n.get_state()
            closed.insert(0,c)


    return n.trace()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    '''YOUR CODE HERE'''
    l = []
    closed = []
    c = problem.getStartState()
    l.insert(0,c)
    closed.insert(0,c)
    n = Node(l, [], 0)
    fringe = util.PriorityQueue()

    while problem.isGoalState(c) != True:
        l = problem.getSuccessors(c)
        for x in l:
            n.add(x)
            if n.get_state() not in closed:
                fringe.push(Node(n.track, n.actions, n.total), n.total)
                closed.insert(0,n.get_state())
            n.pop()
        if len(fringe.heap) == 0:
            break
        n = fringe.pop()
        c = n.get_state()
        closed.insert(0,c)

    if problem.isGoalState(c):
        print("Goal Reached!")
    else:
        print("Goal not found.") 

    return n.trace()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the
    nearest goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    '''YOUR CODE HERE'''
    l = []
    closed = []
    c = problem.getStartState()
    l.insert(0,c)
    closed.insert(0,c)
    n = Node(l, [], 0)
    fringe = util.PriorityQueue()

    while problem.isGoalState(c) != True:
        l = problem.getSuccessors(c)
        for x in l:
            n.add(x)
            if n.get_state() not in closed:
                fringe.push(Node(n.track, n.actions, n.total), n.total + heuristic(c, problem))
                closed.insert(0,n.get_state())
            n.pop()
        if len(fringe.heap) == 0:
            break
        n = fringe.pop()
        c = n.get_state()
        closed.insert(0,c)

    if problem.isGoalState(c):
        print("Goal Reached!")
    else:
        print("Goal not found.") 

    return n.trace()


# Abbreviations
dfts = depthFirstTreeSearch
bfts = breadthFirstTreeSearch
bfs = breadthFirstSearch
dfs = depthFirstSearch
ids = iterativeDeepeningSearch
astar = aStarSearch
ucs = uniformCostSearch
