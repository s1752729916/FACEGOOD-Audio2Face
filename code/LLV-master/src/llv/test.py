import numpy as np
import pandas as pd
from cli import send_one_frame
from buchse import Buchse
path = r'C:\Users\wangy\Desktop\test.csv'
df = pd.read_csv(path)
buchse = Buchse('127.0.0.1', 11111, as_server=False)

for i in range(0,df.shape[0]):
    last = df.iloc[i]
    dict = last.to_dict()
    send_one_frame(buchse,dict,i)
    print(dict)