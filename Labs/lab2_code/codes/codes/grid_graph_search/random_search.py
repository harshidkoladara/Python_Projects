import numpy as np

class RandomSearch :
    def __init__( self, map, start_value=-2, end_value=-3, obstacle_value=-1 ):
        self.map = map

        # Flags to keep track of the states 
        self.flags = np.zeros_like( map )

        h,w = self.map.shape
        self.parents = np.zeros( [h,w,2], dtype=np.int32 )

        # flag : 0, not visited
        # flag : 1, node in the queue
        # flag : 2, node is pulled out of the queue
        
        self.start_value = start_value
        self.end_value = end_value
        self.obstacle_value = obstacle_value

    def is_valid( self, n ):
        ny, nx = n

        # If ny is in the map
        if ny < 0 or ny >= self.map.shape[0] :
            return False

        # If nx is in the map
        if nx < 0 or nx >= self.map.shape[1] :
            return False

        # If n was already visited
        if self.flags[n[0],n[1]] != 0 :
            return False

        # If n is an obstacle
        if self.map[n[0],n[1]] == self.obstacle_value :
            return False

        return True

    def explore( self ):
        # This function assumes that there is only one start point on the grid
        start_position = np.array( np.where( self.map == -2 ) ).reshape([-1,2])[0]

        # We will use the start position as the root of the BFS algorithm and put it
        # as the first element in the queue
        root = start_position
        self.flags[ root[0], root[1] ] = 1
        self.parents[ root[0], root[1], : ] = -1

        # Exploring the graph using the BFS search
        iteration_count = 0

        iteration_count += 1
        print( iteration_count )

        v = root

        found = False
        path = []
        
        while True :
            path.append( [ v[1], v[0] ] )
            map_value = self.map[ v[0], v[1] ]

            if map_value == self.end_value :
                found = True
                break

            neighbors = []

            # Exploring the neighbors of the node
            # Valid moves down, up, left, right
            for p in [ (-1,0), (1,0), (0,-1), (0,1) ] :
                n = np.array( [ v[0]+p[0], v[1]+p[1] ] ) 

                if self.is_valid(n) :
                    neighbors.append(n)
    
            if len( neighbors ) == 0 :
                break

            n = neighbors[ np.random.randint(len(neighbors)) ]
            self.flags[ n[0], n[1] ] = 1
            v = n
    
        return np.array( path )
            
        
