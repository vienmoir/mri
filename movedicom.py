import os


path = '../SK_MRI/MS_dataset_full/MS'


folders = os.listdir(path)
for folder in folders:
    os.makedirs(os.path.join(path, folder, 'dicom'))
    files = os.listdir(os.path.join(path, folder))
    for file in files:
        if file[-4:] != '.txt':
            if file != 'dicom':
                if file != 'tif':
                    os.rename(os.path.join(path, folder, file), os.path.join(path, folder, 'dicom', file))
    print(folder)