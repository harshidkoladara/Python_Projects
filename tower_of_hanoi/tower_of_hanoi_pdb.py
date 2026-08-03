from tower_of_hanoi import *
from priorityq import PQ
import time 

class AStarSearchPDB(Search):
    def __init__(self, start, max_time, debug=False):
        super().__init__(start)
    
        self.end = constructTargetBoard(start.numRods, start.numDisks, start.targetRod)
        self.endHash= self.end.hash()

        self.pdb = PQ()
        self.pdb.update(start)

        self.closedset = {}

        self.gscore = {start.hash() : 0 }
        self.parentTrace[start.hash()] =  {}
        self.db_time = 0        
        self.max_time = max_time
        self.succeed = True
        self.constructPDB()
        
    def constructPDB(self):
        start = time.time()
        while not self.pdb.isEmpty():
            
            if (time.time() - start ) > self.max_time:
                self.succeed = False
                return
            
            current = self.pdb.pop()
            chash = current.hash()

            if current.isFinished():
                self.find_path()
                # return
                end = time.time()
                self.db_time = end - start
                print("Database constructed in {0} s".format(round(end - start), 4))
                print("completed")
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
                self.pdb.update(successor [0], temp_gscore + successor[0].heuristic())


    def find_path(self):
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


if __name__ == "__main__":
    data = []
    n = 1
    while True:
        print("Tower of Hanoi  for disk {}".format(n))
        board = Board(numRods = 4, numDisks = n, targetRod = 3)
        x = AStarSearchPDB(board, max_time = 300)
        x.printPath(True)
        if x.succeed:
            data.append([n, x.numMoves, x.db_time])
        else:
            break
        
        n += 1
    print('---------------------------------------')
    print('|  n  |       Moves     |     Time    |')
    print('---------------------------------------')

    for x in data:
        print(f'|  {x[0]}  |        {x[1]}        |     {round(x[2], 4)} s    |')
    print('-------------------------------------------------------')
