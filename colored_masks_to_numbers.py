# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:04:12 2020

@author: marti
"""
# Packages
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import matplotlib.image as mpimg
from PIL import Image
import scipy
from scipy import ndimage
from pathlib import Path
import os, sys
import glob
import pycm
from pycm import *
import cv2


MASK_PATH = 'IEEE/OCT_images/mask/colour'
MASK_PATH = ''

# reading masks - list of mask 
# 0 stands for reading image as integer type (uint8)
mask = [mpimg.imread(file, 0) for file in sorted(glob.glob(MASK_PATH+'*.png'))] 


imshow(mask[1])
plt.show()
print (np.histogram(mask[1]))
print(np.shape(mask[1]))
print(mask[1])

# dimenisons
width=512
height=1024 
mask_number= 1136 # number of masks in dataset

# color definition
#1st channel red value, 2nd channel green value, 3rd blue, 4th channel alpha is allways equal 255

black = np.array([0, 0, 0, 255])
white = np.array([255, 255, 255, 255])
yellow = np.array([255, 255, 0, 255])
red = np.array([255, 0, 0, 255]) 
blue = np.array([0, 0, 255, 255])
light_blue = np.array([0, 255, 255, 255])
green = np.array([0, 255, 0, 255])
orange = np.array([255, 153, 0, 255])
    
# 8 classes
# joining class values to pixel values (color masks) 
def number_mask (mask):
    mask_new =np.zeros((height, width))
    for i in range (0, height):
        for j in range (0, width):
            if (mask[i,j]==black).all():
                mask_new[i,j]=0 
            elif (mask[i,j]==red).all():
                mask_new[i,j]=1 
            elif (mask[i,j]==yellow).all():
                mask_new[i,j]=2 
            elif (mask[i,j]==green).all():
                mask_new[i,j]=3 
            elif (mask[i,j]==blue).all():
                mask_new[i,j]=4 
            elif (mask[i,j]==light_blue).all():
                mask_new[i,j]=5 
            elif (mask[i,j]==orange).all():
                mask_new[i,j]=6 
            elif (mask[i,j]==white).all():
                mask_new[i,j]=7 
           
    return mask_new

# mask_new - list of new masks after performing conversion from pixel values to class numbers
mask_new = [number_mask(mask[0])]
for k in range (1, 1136):
   mask_new.append(number_mask(mask[k]))
    

# reading list of file id (filename) for masks
# filename is necessary to save with previous name (identical to raw image filename)
all_masks = os.listdir(MASK_PATH)

# saving masks in folder 
for k in range (0, 1136):
    cv2.imwrite(all_masks[k], mask_new[k])