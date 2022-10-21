import numpy as np
import pandas as pd
import re
class fbx_loader:
    def __init__(self):
        pass
    def read_curves(self,fbx_path,name_idx_csv,output_path):
        name_idx_data = pd.read_csv(name_idx_csv).values
        f = open(fbx_path)
        data_str = f.read()
        values_all = []
        names_all = []
        for i in range(0, 274):
            print(i)
            bs_name = name_idx_data[i][0]
            curve_idx = name_idx_data[i][1]

            search_str = 'AnimationCurve([\s\S]*?)'+str(curve_idx)+'([\s\S]*?)KeyValueFloat([\s\S]*?)a:([\s\S]*?)'
            res = re.search(search_str,data_str)
            if res:
                res = res.span()
                print(bs_name)
                end_str_idx = res[1]
                # 匹配数值区域
                res2 = re.search('}',data_str[res[1]:]).span()
                start_str_idx = end_str_idx
                end_str_idx = end_str_idx + res2[1] -1

                values_str = data_str[start_str_idx:end_str_idx]
                values = list(map(float,values_str.split(',')))
                values_all.append(values)
                names_all.append(bs_name)
                print(values)
                print(len(values))
        # 保存dataframe
        data_np = np.array(values_all).T  # (1161,n)
        df = pd.DataFrame(data_np,columns=names_all)
        df.to_csv(output_path,index=False)
    def write_curves(self,old_fbx_path,name_idx_csv,curve_csv,new_fbx_path):
        name_idx_data = pd.read_csv(name_idx_csv).values
        f = open(old_fbx_path)
        data_str = f.read()
        new_data_str = data_str

        # 读取curve数据
        curve_data = pd.read_csv(curve_csv).values # (1161,274)
        for i in range(0, 274):
            print(i)
            bs_name = name_idx_data[i][0]
            curve_idx = name_idx_data[i][1]

            search_str = 'AnimationCurve([\s\S]*?)' + str(curve_idx) + '([\s\S]*?)KeyValueFloat([\s\S]*?)a:([\s\S]*?)'
            res = re.search(search_str, new_data_str)
            if res:
                res = res.span()
                print(bs_name)
                end_str_idx = res[1]
                # 匹配数值区域
                res2 = re.search('}', new_data_str[res[1]:]).span()
                start_str_idx = end_str_idx
                end_str_idx = end_str_idx + res2[1] - 1

                # 构建要输出的字符串
                value_str = ''
                for k in range(curve_data.shape[1]):
                    value_str =  value_str + str(curve_data[k][i]) + ','
                value_str = value_str[:-2] +'\n'
                # print(new_data_str[start_str_idx:end_str_idx])
                print(end_str_idx - start_str_idx)
                print(value_str)

                new_data_str = new_data_str[:start_str_idx] + value_str + new_data_str[end_str_idx:]




        output_file = open(new_fbx_path,'w+')
        output_file.write(new_data_str)
        output_file.close()
        print('write file done: ',output_file)

fbx_path = r'C:\Users\wangy\Desktop\animation_ascii.fbx'
name_idx_csv = r'C:\Users\wangy\Desktop\name_idx.csv'
output_curves_csv = r'C:\Users\wangy\Desktop\curves.csv'
new_output_curves_csv = r'C:\Users\wangy\Desktop\output_curves.csv'
new_fbx_path = r'C:\Users\wangy\Desktop\animation_ascii_new.fbx'
loader = fbx_loader()
# loader.read_curves(fbx_path,name_idx_csv,output_curves_csv)

loader.read_curves(new_fbx_path,name_idx_csv,new_output_curves_csv)
# loader.write_curves(fbx_path,name_idx_csv,output_curves_csv,new_fbx_path)
