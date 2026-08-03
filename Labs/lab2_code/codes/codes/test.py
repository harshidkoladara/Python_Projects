from collections import deque

if __name__=="__main__" :

    queue_obj = deque()

    for i in range( 10 ):
        queue_obj.append( i )

    print( len(queue_obj) )

    print( queue_obj.pop() )