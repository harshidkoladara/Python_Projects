from PIL.Image import MAX_IMAGE_PIXELS
import numpy as np

np.random.seed(4251)

from lab2_code import path_planning
from config import config

from matplotlib import pyplot as pp

from grid_graph_search import BFS, DFS, RandomSearch, GreedySearch, AStar, AStarHeuristic

class module :
    def __init__( self ):
        #self.map = path_planning.generateMap2d(config.map_size)
        self.map = path_planning.generateMap2d_obstacle(config.map_size)[0]

        pp.clf()
        pp.imshow( self.map )
        #pp.show()

        pp.savefig('map.png')

        #print( self.map )

    def RandomSearch( self ):
        rs = RandomSearch( self.map )
        path = rs.explore() 

    def BFS( self ):
        bfs = BFS( self.map )
        path, explore_map, expand_nodes = bfs.explore()
        
        return len(path), expand_nodes

    def DFS( self ):
        dfs = DFS( self.map )
        path, explore_map, expand_nodes = dfs.explore()
        
        return len(path), expand_nodes

    def GreedySearch_Manhattan( self ):
        gs = GreedySearch( self.map, distance='manhattan' )
        path = gs.explore()
        path_planning.plotMap( self.map, path, 'GS_Manhattan' ) 

        print( 'GS_Manhattan', len(path) )

    def GreedySearch_Euclidean( self ):
        gs = GreedySearch( self.map, distance='euclidean' )
        path = gs.explore()
        path_planning.plotMap( self.map, path, 'GS_euclidean' )
        print( 'GS_euclidean', len(path) )

    def AStar_Manhattan( self ):
        astar = AStar( self.map, distance='manhattan' )
        path, g, h, f, expand_nodes = astar.explore()
        
        return len(path), expand_nodes

    def AStar_Euclidean( self ):
        astar = AStar( self.map, distance='euclidean' )
        path, g, h, f, expand_nodes  = astar.explore()
        
        return len(path), expand_nodes

    def AStar_Heuristic_Manhattan( self ):
        astar = AStarHeuristic( self.map, distance='manhattan' )
        path, g, h, f, expand_nodes = astar.explore()
        
        return len(path), expand_nodes

    def AStar_Heuristic_euclidean( self ):
        astar = AStarHeuristic( self.map, distance='euclidean' )
        path, g, h, f, expand_nodes = astar.explore()

        return len(path), expand_nodes

    #def RandomSearch( self ):
        #dfs = DFS( self.map )
        #path = dfs.explore()
    #    astar = AStar( self.map, distance='manhattan' )
    #    path = astar.explore()
    #    path_planning.plotMap( self.map, path, 'A Star' )

if __name__=="__main__" :
    
    # Constructing the 

    bfs_path_length = []
    bfs_expand_nodes = []

    dfs_path_length = []
    dfs_expand_nodes = []

    asm_path_length = []
    asm_expand_nodes = []

    ase_path_length = []
    ase_expand_nodes = []

    ashm_path_length = []
    ashm_expand_nodes = []

    ashe_path_length = []
    ashe_expand_nodes = []

    count = 0

    for i in range( 40 ):
        print('Iteration', i )

        m = module()

        bfs_l,bfs_e = m.BFS()
        dfs_l,dfs_e = m.DFS()
        asm_l,asm_e = m.AStar_Manhattan()
        ase_l,ase_e = m.AStar_Euclidean()
        ashm_l,ashm_e = m.AStar_Heuristic_Manhattan()
        ashe_l,ashe_e = m.AStar_Heuristic_euclidean()

        if ashm_l == 0 or ashe_l == 0 :
            continue

        bfs_path_length.append(bfs_l)
        bfs_expand_nodes.append(bfs_e)

        dfs_path_length.append(dfs_l)
        dfs_expand_nodes.append(dfs_e)

        asm_path_length.append(asm_l)
        asm_expand_nodes.append(asm_e)

        ase_path_length.append(ase_l)
        ase_expand_nodes.append(ase_e)
 
        ashm_path_length.append(ashm_l)
        ashm_expand_nodes.append(ashm_e)

        ashe_path_length.append(ashe_l)
        ashe_expand_nodes.append(ashe_e)

        count = count + 1

        if count == 20 :
            break

    print('BFS', np.mean(bfs_path_length), np.mean(bfs_expand_nodes))
    print('DFS', np.mean(dfs_path_length), np.mean(dfs_expand_nodes))
    print('A* M', np.mean(asm_path_length), np.mean(asm_expand_nodes))
    print('A* E', np.mean(ase_path_length), np.mean(ase_expand_nodes))
    print('A* H M', np.mean(ashm_path_length), np.mean(ashm_expand_nodes))
    print('A* H E', np.mean(ashe_path_length), np.mean(ashe_expand_nodes))