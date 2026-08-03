import itertools
import heapq

class PQ:

    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.REMOVED = -1
        self.counter = itertools.count()
        self.size=0
        self.numAdded = 0
        

    def update (self, game, priority=0):
        hash = game.hash()
        self.numAdded += 1

        if hash in self.entry_finder:
            self.remove_game(game)

        count = next(self.counter)
        entry = [priority, count, game]
        self.entry_finder[hash] = entry
        heapq.heappush(self.pq, entry)
        self.size += 1

    def remove_game (self, task):
        entry = self.entry_finder.pop(task.hash())
        entry[-1] =  self.REMOVED
        self.size -= 1

    def pop(self):
        while len(self.pq) > 0:
            priority, count, task = heapq.heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task.hash()]
                self.size = 1
                return task
        raise KeyError('pop from an empty priority queue' + str(self.size) + str(self.pq))


    def isEmpty(self):
        return self.size == 0