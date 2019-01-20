import pydicom as dicom
import matplotlib.pyplot as plt
import os
import cv2


path = 'D://DWNLDS//test issl itmo//test issl//rs//dicom+roi//rs2 1_03_17/Head+C-Sp+C//AX T2 FLAIR - 12'


files = os.listdir(path)
os.makedirs(os.path.join(path, 'png'))
for file in files:
    image = dicom.dcmread(path).pixel_array
    plt.imsave(os.path.join(path,'png',file + '.png'), image, cmap='gray')
    print(folder)