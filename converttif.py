# -*- coding: utf-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
from functions import *
from stripthem import *

path = 'D:/Uni/mri/mri/u-net/test/gt'


# files = os.listdir(path)
# for file in files:
# 	if file[:-3] == 'png':
# 		im =  cv2.imread(os.path.join(path, file), 0)
# 		im[im != 0] = 255
# 		plt.imsave('D:/Uni/mri/mri/unet/data/test/' + file, im, cmap = 'gray')
# print("done")
files = os.listdir(path)
for i, file in enumerate(files):
	os.rename(os.path.join(path, file), os.path.join(path, str(i) + '.tif'))
print("done")
