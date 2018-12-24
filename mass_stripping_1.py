#import pydicom as dicom
import matplotlib.pyplot as plt
import os
import cv2
import numpy as np
from functions import *


# In[2]:


path = '../SK_MRI/MS_dataset_full/MS'


# In[3]:


brains = []


# In[4]:


folders = os.listdir(path)
for folder in folders:
    files = os.listdir(os.path.join(path, folder,'png'))
    for file in files:
        if file[-6:-4] == '12':
            brains.append(cv2.imread(os.path.join(path,folder,'png',file),3))
    print(folder)


# In[20]:


brr = brains[:20]
len(brr)


# In[21]:


plt.figure(figsize = (100,100))
for i, brain in enumerate(brr):
    sub = len(brr)
    plt.subplot(sub//5, 5, i+1),view(brain)
    plt.xticks([]), plt.yticks([])
plt.show


# In[22]:


segm = []


# In[23]:


for i, img in enumerate(brr):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_OTSU)
    brain_mask = remgar(thresh)
    brain_mask = np.uint8(brain_mask)
    clean = tophat(brain_mask, kernel(10))
    closing_2 = close(clean, 5)
    closing_2 = np.uint8(closing_2)
    mask_2 = floodfill(closing_2)
    segm.append(applymask(img, mask_2))


# In[28]:


plt.figure(figsize = (100,100))
for i, brain in enumerate(segm):
    sub = len(segm)
    plt.subplot(sub//5, 5, i+1),view(brain)
    plt.xticks([]), plt.yticks([])
plt.show


# In[30]:


segm_1 = []
for img in brr:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask_0 = gray < 140
    exp = applymask(img, mask_0)
    gray = cv2.cvtColor(exp, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_OTSU)
    brain_mask = remgar(thresh)
    brain_mask = np.uint8(brain_mask)
    clean = tophat(brain_mask, kernel(10))
    ker = np.ones((3,3), np.uint8) 
    erosion = cv2.erode(clean, ker, iterations=1) 
    closing_2 = close(erosion, 3)
    closing_2 = np.uint8(closing_2)
    mask_2 = floodfill(closing_2)
    exp = remgar(mask_2)
    exp = close(exp, 10)
    exp = floodfill(exp)
    segm_1.append(applymask(img, exp))


# In[194]:


plt.figure(figsize = (100,100))
for i, brain in enumerate(segm_1):
    sub = len(segm_1)
    plt.subplot(sub//5, 5, i+1),view(brain)
    plt.xticks([]), plt.yticks([])
plt.show


# In[188]:


view(brr[9])


# In[105]:


brr_1 = brains[20:40]


# In[195]:


segm_2 = []
for img in brr_1:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask_0 = gray < 140
    exp = applymask(img, mask_0)
    gray = cv2.cvtColor(exp, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_OTSU)
    brain_mask = remgar(thresh)
    brain_mask = np.uint8(brain_mask)
    clean = tophat(brain_mask, kernel(10))
    ker = np.ones((3,3), np.uint8) 
    erosion = cv2.erode(clean, ker, iterations=1) 
    closing_2 = close(erosion, 3)
    closing_2 = np.uint8(closing_2)
    mask_2 = floodfill(closing_2)
    exp = remgar(mask_2)
    exp = close(exp, 10)
    exp = floodfill(exp)
    segm_2.append(applymask(img, exp))


# In[196]:


plt.figure(figsize = (100,100))
for i, brain in enumerate(segm_2):
    sub = len(segm_2)
    plt.subplot(sub//5, 5, i+1),view(brain)
    plt.xticks([]), plt.yticks([])
plt.show


# In[149]:


brr_2 = brains[40:60]


# In[197]:


segm_3 = []
for img in brr_2:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask_0 = gray < 140
    exp = applymask(img, mask_0)
    gray = cv2.cvtColor(exp, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_OTSU)
    brain_mask = remgar(thresh)
    brain_mask = np.uint8(brain_mask)
    clean = tophat(brain_mask, kernel(10))
    ker = np.ones((3,3), np.uint8) 
    erosion = cv2.erode(clean, ker, iterations=1) 
    closing_2 = close(erosion, 3)
    closing_2 = np.uint8(closing_2)
    mask_2 = floodfill(closing_2)
    exp = remgar(mask_2)
    exp = close(exp, 10)
    exp = floodfill(exp)
    segm_3.append(applymask(img, exp))


# In[198]:


plt.figure(figsize = (100,100))
for i, brain in enumerate(segm_3):
    sub = len(segm_3)
    plt.subplot(sub//5, 5, i+1),view(brain)
    plt.xticks([]), plt.yticks([])
plt.show

