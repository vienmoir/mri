import numpy as np
import cv2
from functions import *

def Strip(brain):
    segm = []
    for img in brain:
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
        segm.append(applymask(img, exp))
    return segm

def Show(segm):
    plt.figure(figsize = (100,100))
    for i, brain in enumerate(segm):
        sub = len(segm)
        plt.subplot(sub//5, 5, i+1),view(brain)
        plt.xticks([]), plt.yticks([])
    plt.show