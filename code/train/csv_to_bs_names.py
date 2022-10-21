import numpy as np
import pandas as pd

path = r'C:\Users\wangy\Desktop\test.csv'
df = pd.read_csv(path)
bs_names = df.columns
bs_names_np = np.array(bs_names)
print(bs_names_np.shape)
np.save(r'C:\Users\wangy\Desktop\bs_names.npy',bs_names_np)

