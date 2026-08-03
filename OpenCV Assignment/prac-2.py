import numpy as np
import cv2

def generate_bovw_spatial_histogram(im, locations, clusters, division):

    if im is None:
        print("Error: Unable to load the image")
        return None

    height, width = im.shape[:2]
    num_divisions = np.prod(division)
    histogram = np.zeros((len(clusters), num_divisions), dtype=np.int64)

    if len(division) == 1 and division[0] == 1:
        for loc, cluster_label in zip(locations, clusters):
            x, y = loc
            bin_index = cluster_label
            histogram[bin_index, 0] += 1
    else:
        y_divisions = np.linspace(0, height, division[0] + 1, dtype=int)
        x_divisions = np.linspace(0, width, division[1] + 1, dtype=int)

        for loc, cluster_label in zip(locations, clusters):
            x, y = loc
            x_bin = np.digitize(x, x_divisions) - 1
            y_bin = np.digitize(y, y_divisions) - 1
            bin_index = y_bin * division[1] + x_bin
            histogram[cluster_label, bin_index] += 1

    return histogram.ravel()  

image_path = 'C:/Users/Admin/Documents/ECMM_pract/data/prac2_img.png'
im = cv2.imread(image_path)

if im is None:
    print("Error: Unable to load the image from", image_path)
    exit()

locations = np.array([[10, 20], [30, 40], [50, 60]])
clusters = np.array([0, 1, 2])

divisions = [[1, 1], [2, 2], [3, 3]]

output_filenames = []

for i, division in enumerate(divisions, start=1):
    histogram = generate_bovw_spatial_histogram(im, locations, clusters, division)

    if histogram is None:
        print("Error: Unable to generate histogram for division", i)
        continue

    print("Histogram shape for case", i, ":", histogram.shape)
    print("Histogram for case", i, ":")
    print(histogram)

    filename = f'C:/Users/Admin/Documents/ECMM_pract/prac2_op/histogram_case{i}.npy'
    np.save(filename, histogram)
    output_filenames.append(filename)

print("Output filenames:", output_filenames)
