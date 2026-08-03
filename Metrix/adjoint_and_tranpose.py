import numpy as np


met = np.array(([2, 3, 5, 2, 6],
                [5, 3, 5, 3, 6],
                [6, 7, 4, 2, 8],
                [8, 6, 4, 2, 6],
                [7, 5, 7, 4, 8]))

print('The Metrix is : \n\n',  met)

met_t = met.T


print('\n\n\nThe Transpose  of Metrix is : \n\n',  met_t)


arr_shape = met.shape
cofactor_met = np.empty((5, 5))
for i in range(arr_shape[0]):
    for j in range(arr_shape[1]):
        temp = np.delete(met, i, 0)
        temp = np.delete(temp, j, 1)
        cofactor_met[i][j] = ((-1)**(i+j))*(np.linalg.det(temp))


adj_met = cofactor_met.T
print('\n\n\nThe Adjoint of Metrix is : \n\n',  adj_met)
