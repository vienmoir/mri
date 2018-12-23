# -*- coding: utf-8 -*-
import numpy as np
import pydicom
import cv2
import PIL
import matplotlib.pyplot as plt
import pandas as pd
import os
from showimage import ShowImage


# # Functions

def remgar(image): #remove garbage
    image = image.astype(np.uint8)
    nb_components, output, stats, _ = cv2.connectedComponentsWithStats(image, connectivity = 8)
    sizes = stats[:, -1]

    max_label = 1
    max_size = sizes[1]
    for i in range(2, nb_components):
        if sizes[i] > max_size:
            max_label = i
            max_size = sizes[i]

    cleanimage = np.zeros(output.shape)
    cleanimage[output == max_label] = 255
    return cleanimage

def kernel(num):
    kern = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(num, num))
    return kern

def view(image):
    plt.imshow(image, cmap = 'gray')

def tophat(image, kernel):
    top_hat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
    disconnect = image - top_hat
    new_mask = remgar(disconnect)
    new_mask = np.uint8(new_mask)
    details = new_mask | top_hat
    clean = remgar(details)
    return clean

def close(image, num):
    kernel = np.ones((num,num),np.uint8)
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    closing = closing.astype(np.uint8)
    return closing

def floodfill(image):
    flood = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    cv2.floodFill(flood, mask, (0,0), 255);
    # Invert floodfilled image
    flood_inv = cv2.bitwise_not(flood)
    img = image | flood_inv
    return img

def applymask(image, mask):
    final = image.copy()
    #In a copy of the original image, clear those pixels that don't correspond to the brain
    final[mask == False] = (0,0,0)
    return final

## Image

path = ('../SK_MRI/MS_dataset_full/MS/')

img = cv2.imread(path + '01_1/IM000019.png',3) #read img
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

plt.figure(figsize=(10, 10))
plt.subplot(241),plt.imshow(img)
plt.title('Original image'), plt.xticks([]), plt.yticks([])
plt.subplot(242),plt.imshow(brain_1)
plt.title('Brain image'), plt.xticks([]), plt.yticks([])
plt.subplot(243),plt.imshow(thresh,cmap = 'gray')
plt.title('Binary image'), plt.xticks([]), plt.yticks([])
plt.subplot(244),plt.imshow(mask_1, cmap = 'gray')
plt.title('Mask image'),  plt.xticks([]), plt.yticks([])

plt.figure(figsize=(10, 10))
plt.subplot(241),plt.imshow(img)
plt.title('Original image'), plt.xticks([]), plt.yticks([])
plt.subplot(242),plt.imshow(brain_2)
plt.title('Brain image'), plt.xticks([]), plt.yticks([])
plt.subplot(243),plt.imshow(thresh,cmap = 'gray')
plt.title('Binary image'), plt.xticks([]), plt.yticks([])
plt.subplot(244),plt.imshow(mask_2, cmap = 'gray')
plt.title('Mask image'),  plt.xticks([]), plt.yticks([])