import matplotlib.pyplot as plt
import os
import cv2

from functions import *
from stripthem import *


path = '../SK_MRI/MS_dataset_full/MS'


# In[ ]:


folders = os.listdir(path)
for folder in folders:
    files = os.listdir(os.path.join(path, folder, 'tif'))
    for file in files:
        if file[-6:] == '09.tif':
            im = cv2.imread(os.path.join(path,folder,'tif',file))
            row, col = im.shape[:2]
            bsize = 32
            bim = cv2.copyMakeBorder(im, top = 0, bottom = 0, left = bsize, right = bsize, 
                                     borderType = cv2.BORDER_CONSTANT, value = [0,0,0])
            plt.imsave('../dataset/masks/' + file, bim, cmap='gray')
    print(folder)


# In[ ]:


folders = os.listdir(path)
for folder in folders:
    files = os.listdir(os.path.join(path, folder, 'png'))
    for file in files:
        if file[-6:] == '09.png':
            im = cv2.imread(os.path.join(path,folder,'png',file))
            row, col = im.shape[:2]
            bsize = 32
            bim = cv2.copyMakeBorder(im, top = 0, bottom = 0, left = bsize, right = bsize, 
                                     borderType = cv2.BORDER_CONSTANT, value = [0,0,0])
            plt.imsave('../dataset/heads/' + folder + '0009.tif', bim, cmap='gray')
    print(folder)


# In[29]:


path = '../dataset/heads'
slices = []
files = os.listdir(path)
for file in files:
    im = cv2.imread(os.path.join(path,file))
    res, _ = strip_one(im)
    plt.imsave('../dataset/brains/' + file, res, cmap='gray')