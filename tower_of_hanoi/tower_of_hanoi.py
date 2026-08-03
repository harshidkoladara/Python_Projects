import copy
import time
import queue
from board import *

import itertools
import heapq
from priorityq import PQ


class Search:
    def __init__(self, start):
        self.parentTrace = {}
        self.start = start
        self.gamePath = []
        self.movePath = []
        self.numMoves = 0
        self.end = None


    
    def unwindPath(self):
        if self.end:
            target = self.end
        else:
            target = constructTargetBoard(self.start.numRods, self.start.numDisks, self.start.targetRod)

        startHash = self.start.hash()
        nextHash = target.hash()

        self.gamePath = []
        self.movePath = []

        if not startHash == nextHash:
            while (True):
                constructBoard(nextHash, self.start.numRods, self.start.numDisks, self.start.targetRod).printBoard()
                self.gamePath.insert(0, constructBoard(nextHash, self.start.numRods, self.start.numDisks, self.start.targetRod))

                if startHash == nextHash:
                    break
                else:
                    moves = self.parentTrace[nextHash][1]
                    self.movePath.insert(0, moves)
                    nextHash= self.parentTrace[nextHash][0]

        self.numMoves += len(self.movePath)


    def printPath(self, verbose=False):
        if verbose:
            counter = 0

            for i in range(len(self.gamePath)):

                if counter == 0:
                    print("ORIGINAL")
                    print("Heurstic = " + str(self.gamePath[i].heuristic()) + " : Actual Dist= " + str(len(self.gamePath) - counter - 1))
                    self.gamePath[i].printBoard()
                else:
                    print("MOVE " + str(counter) + " : " + str(self.movePath[counter - 1]))
                    print("Heurstic = " + str(self.gamePath[i].heuristic()) + " Actual Dist = " + str(len(self.gamePath) - counter -1))
                    self.gamePath[i].printBoard()
                    print ("-------------------------------------------------")
                counter += 1
        else:
            for i in range(len(self.movePath)):
                print("MOVE " + str(i+1) + " : " + str(self.movePath[i]))

        return counter

class DFSSearch(Search):

    def __init__(self, start):
        super().__init__(start)
        self.search()

    
    def search(self):
        self.parentTrace = {}

        stack = [(self.start, (0,0,0))]

        while(not len(stack) == 0):
            game = stack.pop()[0]
            hash = game.hash()
            
            if game.isFinished():
                self.unwindPath()
                return

            successors = game.successors()

            successors[:] = filter(lambda x: x[0].hash() not in self.parentTrace, successors)

            for successor in successors:
                self.parentTrace[successor[0].hash()] = (hash, successor[1])
                stack.append(successor)


class BFSSearch(Search):
    def __init__(self, start, end=None):
        super().__init__(start)

        if end is None:
            self.end = constructTargetBoard(start.numRods, start.numDisks, start.targetRod)
        else:
            self.end = end

        self.endHash = self.end.hash()
        self.parentTrace = {}
        self.search()

    
    def search(self):
        self.parentTrace = {}

        q = queue.Queue()

        q.put((self.start, (0,0,0)))

        while q.empty():
            game = q.get()[0]
            hash = game.hash()
            
            if game.isFinished():
                self.unwindPath()
                return

            successors = game.successors()

            successors[:] = filter(lambda x: x[0].hash() not in self.parentTrace, successors)

            for successor in successors:
                self.parentTrace[successor[0].hash()] = (hash, successor[1])
                q.put(successor)



class AStarSearch(Search):
    def __init__(self, start, debug=False):
        super().__init__(start)
    
        self.end = constructTargetBoard(start.numRods, start.numDisks, start.targetRod)
        self.endHash= self.end.hash()

        self.openset = PQ()
        self.openset.update(start)

        self.closedset = {}

        self.gscore = {start.hash() : 0 }
        self.parentTrace[start.hash()] =  {}
        self.search()
        
    
    def search(self):

        while not self.openset.isEmpty():
            current = self.openset.pop()
            chash = current.hash()

            if current.isFinished():
                self.unwindPath()
                return

            sucessors = current.successors()
            self.closedset[chash] = True

            for successor in sucessors:
                shash = successor[0].hash()

                if shash in self.closedset:
                    continue

                temp_gscore = self.gscore[chash] + 1

                if shash not in self.gscore:
                    self.gscore[shash] = temp_gscore

                elif temp_gscore == self.gscore[shash]:
                    continue

                else:
                    self.gscore[shash] =  temp_gscore

                self.parentTrace[shash] = (chash, successor[1])
                self.openset.update(successor [0], temp_gscore + successor[0].heuristic())


if __name__ == "__main__":

    data = []
    for n in range(1, 10):
        board = Board(numRods = 4, numDisks = n, targetRod = 3)

        print("----------------------------------------  DFS Algorithm for Disk {} ---------------------------------------- ".format(n))
        start_bfs = time.time()
        m_bfs = DFSSearch (board).printPath(True)
        end_bfs = time.time()
        print("----------------------------------------  A* Algorithm for Disk {} ---------------------------------------- ".format(n))
        start_a_star = time.time()
        m_a_star = AStarSearch(board).printPath(True)
        end_a_star = time.time()

        data.append([n, m_bfs, end_bfs-start_bfs, m_a_star, end_a_star-start_a_star])


    print('------------------------------------------------------------------------')
    print('|  n  |     DFS Moves   |    DFS Time    |     A* Moves     |     A* Time    |')
    print('------------------------------------------------------------------------')

    for x in data:
        print(f'|  {x[0]}  |        {x[1]}        |     {round(x[2], 4)} s    |        {x[3]}         |    {round(x[4], 4)} s    |')
    print('------------------------------------------------------------------------')

        