# -*- coding: utf-8 -*-

import numpy as np
import cv2
import matplotlib.pyplot as plt

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
