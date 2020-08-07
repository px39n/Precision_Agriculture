
# Python program to print prime factors

import math
from sklearn import cluster
from skimage import data
import numpy as np
import cv2

def factors_number(n):
# A function to print all prime factors of
# a given number n

    n2 = int(n/2)
    fn = []
    for x in range(2,n2+1):
        if n%x == 0:
            if not([int(n/x), int(x)] in fn):
                fn.append([int(x), int(n/x)]) #lower member of factor pair #upper member of factor pair
    if fn == []: fn.append([1, n])
    return fn

def rgb2gray(rgb):
# RGB array  to gray
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def km_clust(array, n_clusters):
## KMeans Segmentation Image

    # Create a line array, the lazy way
    if len(array.shape) == 3:
        X = array.reshape((-1, array.shape[-1]))
    else :
        X = array.reshape((-1, 1))


    # Define the k-means clustering problem
    k_m = cluster.KMeans(n_clusters = n_clusters, n_init=4)
    # Solve the k-means clustering problem
    k_m.fit(X)
    # Get the coordinates of the clusters centres as a 1D array
    values = k_m.cluster_centers_.squeeze()
    # Get the label of each point
    labels = k_m.labels_

    return(values, labels, k_m)

def kmeans_image(Z, n_clusters, weight_positional = 0):
    #Kmeans in Image with dimensional position
    #n_cluster is the number of n_clusters
    #weight_positional is you can put weights to coordinates, i.e. Kmeans with two more dimensionas.

    grid = np.indices((Z.shape[0], Z.shape[1]))
    grid = grid.astype(float)
    grid[0] = grid[0] / grid[0].max() * weight_positional
    grid[1] = grid[1] / grid[1].max() * weight_positional

    if len(Z.shape) == 3:

        img = np.zeros((Z.shape[0], Z.shape[1], Z.shape[2] + 2))
        img[:, :, :3] = Z#[:,:,1]
        img[:, :, 3] = grid[0]
        img[:, :, 4] = grid[1]

    else:

        img = np.zeros((Z.shape[0], Z.shape[1], 3))
        img[:, :, 0] = Z#[:,:,1]
        img[:, :, 1] = grid[0]
        img[:, :, 2] = grid[1]

    # Group similar grey levels using 8 clusters
    values, labels, k_m = km_clust(img, n_clusters = n_clusters)
    print (values.shape)
    print (labels.shape)
    # Create the segmented array from labels and values
    img_segm = np.array([values[label][:3] for label in labels]) #np.choose(labels, values)
    # Reshape the array as the original image
    img_segm.shape = img[:,:,:3].shape

    return img_segm


def order_points_rect(pts):
	# initialzie a list of coordinates that will be ordered
	# such that the first entry in the list is the top-left,
	# the second entry is the top-right,
    # the third is the bottom-right, and
    #the fourth is the bottom-left
	rect = np.zeros((4, 2), dtype = "float32")
	# the top-left point will have the smallest sum, whereas
	# the bottom-right point will have the largest sum
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]
	# now, compute the difference between the points, the
	# top-right point will have the smallest difference,
	# whereas the bottom-left will have the largest difference
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]
	# return the ordered coordinates
	return rect


def perspectiveTransform(Points):
    #Transform cuadrilater image segmentation to rectangle image
    # Return Matrix Transform
    Points = np.array(Points)
    Points_order = order_points_rect(Points)
    #dst = np.asarray([[0, 0], [0, 1], [1, 1], [1, 0]], dtype = "float32")

    (tl, tr, br, bl) = Points_order
    # compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # x-coordiates or the top-right and top-left x-coordinates
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    # compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    # now that we have the dimensions of the new image, construct
    # the set of destination points to obtain a "birds eye view",
    # (i.e. top-down view) of the image, again specifying points
    # in the top-left, top-right, bottom-right, and bottom-left
    # order
    dst = np.array([
        [0, 0],
        [maxWidth , 0],
        [maxWidth , maxHeight ],
        [0, maxHeight ]], dtype = "float32")

    M = cv2.getPerspectiveTransform(Points_order, dst)
    return M, maxWidth, maxHeight

def subdivision_rect(factors, maxWidth, maxHeight):
    ## From a rect (top-left, top-right, bottom-right, bottom-left) subidive in rectangle

    #factors = factors_number(n_divide)[-1] # First factor is smaller

    #if maxWidth > maxHeight:
    #    split_Width = [maxWidth / factors[1] * i for i in range(factors[1] + 1)]
    #    split_Height = [maxHeight / factors[0] * i for i in range(factors[0] + 1)]
    #else:
    #    split_Width = [maxWidth / factors[0] * i for i in range(factors[0] + 1)]
    #    split_Height = [maxHeight / factors[1] * i for i in range(factors[1] + 1)]
    split_Width = [maxWidth / factors[0] * i for i in range(factors[0] + 1)]
    split_Height = [maxHeight / factors[1] * i for i in range(factors[1] + 1)]

    sub_division = []
    for j in range(len(split_Height) - 1):
        for i in range(len(split_Width) - 1):

            sub_division.append([(split_Width[i], split_Height[j]),
                                 (split_Width[i+1], split_Height[j]),
                                 (split_Width[i+1], split_Height[j+1]),
                                 (split_Width[i], split_Height[j+1])])

    return np.array(sub_division)
