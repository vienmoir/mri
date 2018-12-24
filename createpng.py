import pydicom as dicom
import matplotlib.pyplot as plt
import os
import cv2


path = '../SK_MRI/MS_dataset_full/MS'


folders = os.listdir(path)
for folder in folders:
    os.makedirs(os.path.join(path, folder, 'png'))
    files = os.listdir(os.path.join(path, folder, 'dicom'))
    for file in files:
        image = dicom.dcmread(os.path.join(path, folder,'dicom', file)).pixel_array
        plt.imsave(os.path.join(path,folder,'png',file + '.png'), image, cmap='gray')
    print(folder)