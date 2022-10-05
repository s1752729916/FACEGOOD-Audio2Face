import os
import numpy as np
project_dir = r'C:\Users\wangy\Desktop\ProjectsSmq\FACEGOOD-Audio2Face'
data_dir = os.path.join(project_dir,r'DataForAudio2Bs\train\dataSet1')

x_train = np.load(os.path.join(data_dir,'train_data.npy')) # (24370,32,64,1)
x_train = x_train[:2200] #(2200,32,64,1)
# y_train = np.load(os.path.join(data_dir,'train_label_var.npy'))
x_val = np.load(os.path.join(data_dir,'val_data.npy')) # (1000,32,64,1)
print(111)