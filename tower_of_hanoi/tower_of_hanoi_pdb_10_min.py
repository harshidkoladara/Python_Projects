from tower_of_hanoi_pdb import *

if __name__ == "__main__":
    data = []
    n = 1
    while True:
        print("Tower of Hanoi  for disk {}".format(n))
        board = Board(numRods = 4, numDisks = n, targetRod = 3)
        x = AStarSearchPDB(board, max_time = 600)
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