import os


path = '../SK_MRI/MS_dataset_full/MS'


folders = os.listdir(path)
for folder in folders:
    os.makedirs(os.path.join(path, folder, 'tif'))
    files = os.listdir(os.path.join(path, folder))
    for file in files:
        if file[-4:] == '.tif':
            os.rename(os.path.join(path, folder, file), os.path.join(path, folder, 'tif', file))
            #print(file)
    print(folder)