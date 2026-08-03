import operator
import numpy as np
from .distances import distances

class Node :
    def __init__( self, n, p ):
        self.position = n # Node
        self.parent = p # Parent

        self.g = 0 # Cost from start to this Node
        self.h = 0 # Estimated cost from this node to goal
        self.f = 0 # Estimated cost of path containing this node
    
    def __eq__( self, o ):
        return ( self.position == o.position ).all()

class AStar :
    def __init__( self, map, start_value=-2, end_value=-3, obstacle_value=-1, distance='euclidean' ):
        self.map = map

        h,w = self.map.shape
        self.parents = np.zeros( [h,w,2], dtype=np.int32 )

        # Cost to each a node from start
        self.g = np.zeros_like( map )
        # Estimated cost from each node to reach the goal
        self.h = np.zeros_like( map )
        # Estimated cost of a path going from start to goal going through each node
        self.f = np.zeros_like( map )

        # flag : 0, not visited
        # flag : 1, node in the queue
        # flag : 2, node is pulled out of the queue
        
        self.start_value = start_value
        self.end_value = end_value
        self.obstacle_value = obstacle_value

        # Setting the distance
        self.distance = distances[distance]

    def is_valid( self, n ):
        ny, nx = n

        # If ny is in the map
        if ny < 0 or ny >= self.map.shape[0] :
            return False

        # If nx is in the map
        if nx < 0 or nx >= self.map.shape[1] :
            return False

        # If n is an obstacle
        if self.map[n[0],n[1]] == self.obstacle_value :
            return False

        return True

    def explore( self ):
        # This function assumes that there is only one start point on the grid

        # Finding the start position in the map
        start_position = np.array( np.where( self.map == -2 ) ).reshape([-1,2])[0]

        # Finding the end poisition in the map, this is needed for calculating the distance
        # for selecting the closest node to the target
        goal_position = np.array( np.where( self.map == -3 ) ).reshape([-1,2])[0]

        # We will use the start position as the root of the BFS algorithm and put it
        # as the first element in the queue
        root = start_position
        self.parents[ root[0], root[1], : ] = -1

        # Initializing open and closed lists
        open_list = []
        closed_list = []

        open_list.append( Node(start_position, None) )

        count = 0
        
        while len(open_list) > 0 :
            #print( len(open_list), len(closed_list) )
            # From the open list, we want to select the node that has the lowest f
            # See above for the definition of f

            v = open_list[0]
            
            idx = 0

            for ii, n in enumerate(open_list):
                if n.f < v.f :
                    v = n

            self.g[ v.position[0], v.position[1] ] = v.g
            self.h[ v.position[0], v.position[1] ] = v.h
            self.f[ v.position[0], v.position[1] ] = v.f

            count = count + 1 

            #print( v.position )
                    
            open_list.remove( v )
            closed_list.append( v )

            map_value = self.map[ v.position[0], v.position[1] ]

            if map_value == self.end_value :
                # Found the goal, do something
                path = []

                current = v
                while current is not None :
                    path.append( current.position[::-1] )
                    current = current.parent
                path = path[::-1]
                break

            children = []
            # Exploring the neighbors of the node
            # Valid moves down, up, left, right
            for pos in [ (-1,0), (1,0), (0,-1), (0,1) ] :
                n = np.array( [ v.position[0]+pos[0], v.position[1]+pos[1] ] )
                intermediate_node = Node(n,v)
                if self.is_valid(n) and not intermediate_node in closed_list  :
                    children.append( Node(n,v))

            for c in children :
                c.g = v.g + 1
                c.h = self.distance( c.position, goal_position )
                c.f = c.g + c.h

                if c in open_list :
                    idx = open_list.index(c)
                    if c.g >= open_list[idx].g :
                        continue

                open_list.append( c )

        return np.array(path), self.g, self.h, self.f, count
        
