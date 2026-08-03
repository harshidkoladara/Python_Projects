from PIL.Image import MAX_IMAGE_PIXELS
import numpy as np

np.random.seed(1434)

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
        path_planning.plotMap( self.map, path, 'RandomSearch' )

    def BFS( self ):
        bfs = BFS( self.map )
        path, explore_map, expand_nodes = bfs.explore()
        path_planning.plotMap( self.map, path, 'BFS' )

        print('BFS', len(path), expand_nodes )

        pp.clf()
        pp.matshow( explore_map )
        pp.savefig('BFS_Explore_map.png')

    def DFS( self ):
        dfs = DFS( self.map )
        path, explore_map, expand_nodes = dfs.explore()
        path_planning.plotMap( self.map, path, 'DFS', expand_nodes )

        pp.clf()
        pp.matshow( explore_map )
        pp.savefig('DFS_Explore_map.png')

        print('DFS', len(path) )

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
        path_planning.plotMap( self.map, path, 'AStar_Manhattan' ) 

        pp.clf()
        pp.matshow( g )
        pp.title('G')
        pp.savefig('AStar_Manhattan_g.png')

        pp.clf()
        pp.matshow( h )
        pp.title('H')
        pp.savefig('AStar_Manhattan_h.png')

        pp.clf()
        pp.matshow( f )
        pp.title('F')
        pp.savefig('AStar_Manhattan_f.png')

        print( 'AStar_Manhattan', len(path), expand_nodes )

    def AStar_Euclidean( self ):
        astar = AStar( self.map, distance='euclidean' )
        path, g, h, f, expand_nodes  = astar.explore()
        path_planning.plotMap( self.map, path, 'AStar_euclidean' )
        print( 'AStar_euclidean', len(path), expand_nodes )

        pp.clf()
        pp.matshow( g )
        pp.title('G')
        pp.savefig('AStar_euclidean_g.png')

        pp.clf()
        pp.matshow( h )
        pp.title('H')
        pp.savefig('AStar_euclidean_h.png')

        pp.clf()
        pp.matshow( f )
        pp.title('F')
        pp.savefig('AStar_euclidean_f.png')

    def AStar_Heuristic_Manhattan( self ):
        astar = AStarHeuristic( self.map, distance='manhattan' )
        path, g, h, f, expand_nodes = astar.explore()
        #path_planning.plotMap( self.map, path, 'AStar_Heuristic_Manhattan' ) 

        pp.clf()
        pp.matshow( g )
        pp.title('G')
        pp.savefig('AStar_Heuristic_Manhattan_g.png')

        pp.clf()
        pp.matshow( h )
        pp.title('H')
        pp.savefig('AStar_Heuristic_Manhattan_h.png')

        pp.clf()
        pp.matshow( f )
        pp.title('F')
        pp.savefig('AStar_Heuristic_Manhattan_f.png')

        print( 'AStar_Heuristic_Manhattan', len(path), expand_nodes )

    def AStar_Heuristic_euclidean( self ):
        astar = AStarHeuristic( self.map, distance='euclidean' )
        path, g, h, f, expand_nodes = astar.explore()

        path_planning.plotMap( self.map, path, 'AStar_Heuristic_euclidean' ) 

        pp.clf()
        pp.matshow( g )
        pp.title('G')
        pp.savefig('AStar_Heuristic_euclidean_g.png')

        pp.clf()
        pp.matshow( h )
        pp.title('H')
        pp.savefig('AStar_Heuristic_euclidean_h.png')

        pp.clf()
        pp.matshow( f )
        pp.title('F')
        pp.savefig('AStar_Heuristic_euclidean_f.png')

        print( 'AStar_Heuristic_euclidean', len(path), expand_nodes )

    #def RandomSearch( self ):
        #dfs = DFS( self.map )
        #path = dfs.explore()
    #    astar = AStar( self.map, distance='manhattan' )
    #    path = astar.explore()
    #    path_planning.plotMap( self.map, path, 'A Star' )

if __name__=="__main__" :
    
    # Constructing the 
    m = module()

    m.RandomSearch()
    m.BFS()
    m.DFS()
    m.GreedySearch_Manhattan()
    m.GreedySearch_Euclidean()
    m.AStar_Manhattan()
    m.AStar_Euclidean()
    m.AStar_Heuristic_Manhattan()
    m.AStar_Heuristic_euclidean()
    
