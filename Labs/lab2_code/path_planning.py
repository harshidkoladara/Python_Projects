"""
A* ALGORITHM PATH PLANNING

"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
plt.interactive(False)

PERCENT_OF_OBSTACLES = 0.9


def generateMap2d_obstacle(SIZE_):

    SIZE_x, SIZE_y = SIZE_[0], SIZE_[1] # GET SHAPE
    generated_map2d = generateMap2d(SIZE_) # Generate the map

    generated_map2d[generated_map2d==-2] = 0 
    generated_map2d[generated_map2d==-3] = 0

    # add random obstacles
    x_top = [np.random.randint(5, 3*SIZE_x//10-2), np.random.randint(7*SIZE_x//10+3, SIZE_x-5)] 
    y_top = np.random.randint(7*SIZE_y//10 + 3, SIZE_y - 5)
    x_bot = np.random.randint(3, 3*SIZE_x//10-5), np.random.randint(7*SIZE_x//10+3, SIZE_x-5)
    y_bot = np.random.randint(5, SIZE_y//5 - 3)

    generated_map2d[y_bot, x_bot[0]:x_bot[1]+1] = -1 # add bottom points in generated map
    generated_map2d[y_top, x_top[0]:x_top[1]+1] = -1 # add top points in generated map

    min_x = (x_bot[0]+x_bot[1])//2 # min_x 
    max_x = (x_top[0]+x_top[1])//2 # max_x

    # swapping if min_x is greated then max_x
    if min_x > max_x:
        temp_x = min_x
        min_x = max_x
        max_x = temp_x

    # if min_x == max_x then adding 1 to max_x
    if max_x == min_x:
        max_x = max_x+1

    # finding start point
    generated_map2d[y_bot:y_top, min_x:max_x] = -1
    start_p = [np.random.randint(0, SIZE_x//2 - 4), np.random.randint(y_bot+1, y_top-1)]

    # finding end point
    generated_map2d[start_p[1], start_p[0]] = -2
    goal_p = [np.random.randint(SIZE_x//2 + 4, SIZE_x - 3), np.random.randint(y_bot+1, y_top-1)]

    generated_map2d[goal_p[1],goal_p[0]] = -3
    return generated_map2d, [y_top, y_bot, min_x]


def generateMap2d(SIZE_):
    
    SIZE_x, SIZE_y = SIZE_[0], SIZE_[1] # GET SHAPE

    generated_map2d = np.random.rand(SIZE_y, SIZE_x)

    generated_map2d[generated_map2d <= PERCENT_OF_OBSTACLES] = 0
    generated_map2d[generated_map2d > PERCENT_OF_OBSTACLES] = -1

    y_loc, x_loc = [np.random.randint(0, SIZE_x-1, 2), np.random.randint(0, SIZE_y-1, 2)] # Generating random points
    while (y_loc[0] == y_loc[1]) and (x_loc[0] == x_loc[1]):
        y_loc, x_loc = [np.random.randint(0, SIZE_x-1,2), np.random.randint(0, SIZE_y-1, 2)]

    generated_map2d[x_loc[0]][y_loc[0]] = -2 # changing value to -2
    generated_map2d[x_loc[1]][y_loc[1]] = -3 # changing value to -3

    return generated_map2d


def plotMap(map2d_, path_, title_ =''):   
    
    colors_nn = int(map2d_.max())
    colors = cm.winter(np.linspace(0, 1, colors_nn))

    colors_map_2d = [[[] for _ in range(map2d_.shape[1])] for _ in range(map2d_.shape[0])]
    
    # Assign RGB Val for starting point and ending point
    loc_start, loc_end = np.where(map2d_ == -2), np.where(map2d_ == -3)
    
    colors_map_2d[loc_start[0][0]][loc_start[1][0]] = [.0, .0, .0, 1.0]  # black
    colors_map_2d[loc_end[0][0]][loc_end[1][0]] = [.0, .0, .0, .0]  # white

    # Assign RGB Val for obstacle
    loc_obstacle = np.where(map2d_ == -1)
    for i_pos_obstacle in range(len(loc_obstacle[0])):
        colors_map_2d[loc_obstacle[0][i_pos_obstacle]][loc_obstacle[1][i_pos_obstacle]] = [1.0, .0, .0, 1.0]

    # Assign 0
    loc_zero = np.where(map2d_ == 0)
    for i_pos_zero in range(len(loc_zero[0])):
        colors_map_2d[loc_zero[0][i_pos_zero]][loc_zero[1][i_pos_zero]] = [1.0, 1.0, 1.0, 1.0]

    # Assign Expanded nodes
    loc_expand = np.where(map2d_>0)
    for ipos_expand in range(len(loc_expand[0])):
        _idx_ = int(map2d_[loc_expand[0][ipos_expand]][loc_expand[1][ipos_expand]]-1)
        colors_map_2d[loc_expand[0][ipos_expand]][loc_expand[1][ipos_expand]] = colors[_idx_]

    for i_row in range(len(colors_map_2d)):
        for i_col in range(len(colors_map_2d[i_row])):
            if colors_map_2d[i_row][i_col] == []:
                colors_map_2d[i_row][i_col] = [1.0, 0.0, 0.0, 1.0]
                
    path = path_.T.tolist()
    
    plt.figure()
    plt.title(title_)
    plt.imshow(colors_map_2d, interpolation='nearest')
    plt.colorbar()
    plt.plot(path[:][0],path[:][1], color='magenta',linewidth=2.5)
    plt.show()


if __name__ == "__main__":
    # create a map with obstacles randomly distributed
    _map_ = generateMap2d([90, 90])
    plt.clf()
    plt.imshow(_map_)
    plt.show()

    # map with rotated-H shape obstacle and obstacles randomly distributed
    map_h_object, info = generateMap2d_obstacle([90, 90])

    # environment information
    print("map info: ")
    print("y top: ", info[0])
    print("t bot: ", info[1])
    print("x wall: ", info[2])

    plt.clf()
    plt.imshow(map_h_object)
    plt.show()


    # example for a solved_map
    example_solved_map = map_h_object
    example_solved_path = np.array([[xx, xx*2] if xx % 2 == 0 else [xx, xx+1] for xx in range(20)])

    print("path")
    for xx in example_solved_path:
        print(xx, end=" -> ")

    plotMap(example_solved_map, example_solved_path)


