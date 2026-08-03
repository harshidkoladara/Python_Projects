import numpy as np
from scipy.signal import convolve2d
from PIL import Image

def compute_gradient_magnitude(gr_im, kx, ky):
    gradient_x = convolve2d(gr_im, kx, mode='same', boundary='symm')
    gradient_y = convolve2d(gr_im, ky, mode='same', boundary='symm')
    
    gradient_magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)
    
    return gradient_magnitude.astype(np.float64)

def compute_gradient_direction(gr_im, kx, ky):
    gradient_x = convolve2d(gr_im, kx, mode='same', boundary='symm')
    gradient_y = convolve2d(gr_im, ky, mode='same', boundary='symm')
    
    gradient_direction = np.arctan2(gradient_y, gradient_x)
    
    return gradient_direction.astype(np.float64)

image_path = r'C:\Users\Admin\Documents\ECMM_pract\data\shapes.png'
try:
    image = Image.open(image_path).convert('L')  
except FileNotFoundError:
    print(f"File '{image_path}' not found. Please check the file path.")
    exit()

gr_im = np.array(image)

kx = np.array([[1, 7, -1],
               [4, 7, -2],
               [1, 7, -1]], dtype=int)
ky = np.array([[1, 4, 1],
               [7, 7, 7],
               [-1, -2, -1]], dtype=int)

gradient_magnitude = compute_gradient_magnitude(gr_im, kx, ky)
gradient_direction = compute_gradient_direction(gr_im, kx, ky)

print("Gradient Magnitude:")
print(gradient_magnitude)
print("\nGradient Direction (in radians):")
print(gradient_direction)
