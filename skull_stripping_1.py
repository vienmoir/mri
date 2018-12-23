# -*- coding: utf-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
from functions import *

## Image

path = ('../SK_MRI/MS_dataset_full/MS/')

img = cv2.imread(path + '01_1/IM000015.png',3) #read img
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grayscale

ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_OTSU)

brain_mask = remgar(thresh)
#view(brain_mask)

brain_mask = np.uint8(brain_mask)

## Baseline

closing_1 = close(brain_mask, 5)
#view(closing)

mask_1 = floodfill(closing_1)
#view(mask_1)

brain_1 = applymask(img, mask_1)
#view(brain_1)


# # Baseline + Tophat

#ker = kernel(10)
clean = tophat(brain_mask, kernel(10))
#view(clean)

closing_2 = close(clean, 5)
#view(closing_2)

closing_2 = np.uint8(closing_2)
mask_2 = floodfill(closing_2)
#view(mask_1)

brain_2 = applymask(img, mask_2)

## Results

plt.figure(figsize=(10, 20))
plt.subplot(241),plt.imshow(img)
plt.title('Original image'), plt.xticks([]), plt.yticks([])
plt.subplot(242),plt.imshow(brain_1)
plt.title('Brain image'), plt.xticks([]), plt.yticks([])
plt.subplot(243),plt.imshow(thresh,cmap = 'gray')
plt.title('Binary image'), plt.xticks([]), plt.yticks([])
plt.subplot(244),plt.imshow(mask_1, cmap = 'gray')
plt.title('Mask image'),  plt.xticks([]), plt.yticks([])
plt.subplot(245),plt.imshow(img)
plt.title('Original image'), plt.xticks([]), plt.yticks([])
plt.subplot(246),plt.imshow(brain_2)
plt.title('Brain image'), plt.xticks([]), plt.yticks([])
plt.subplot(247),plt.imshow(thresh,cmap = 'gray')
plt.title('Binary image'), plt.xticks([]), plt.yticks([])
plt.subplot(248),plt.imshow(mask_2, cmap = 'gray')
plt.title('Mask image'),  plt.xticks([]), plt.yticks([])
plt.show()

print("success")