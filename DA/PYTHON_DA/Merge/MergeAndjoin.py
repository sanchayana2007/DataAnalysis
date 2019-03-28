import pandas as pd
import numpy as np
import glob
all_data = pd.DataFrame()
for f in glob.glob("sales*.xlsx"):
    df = pd.read_excel(f)
    #print(df.head())
    all_data = all_data.append(df,ignore_index=True)
print("ADD ROWS OF SAME KINDA DATAS: UNION")
print(all_data.head())
print("DESCRIBE : Provide min.max.coint,std deviation ")
print(all_data.describe())


print("ADD COULMNS USING A COMMON MATCHING DATA : JOIN")
print("TABLE 2 : customer status with name")
status = pd.read_excel("customer-status.xlsx")
print(status.head())
print("After JOIN")
#all_data_st = pd.merge(all_data, status, how='left')
all_data_st = pd.merge(all_data, status[['status',"account number"]],left_on="account number",right_on="account number", how='inner')
print(all_data_st.head())
print("SORT: Status")
s =all_data_st.sort_values(by=["status"]).head()
print(s)
print("GOURPBY:")
s =all_data_st.groupby(["status"])["quantity","unit price","ext price"].agg([np.sum,np.mean, np.std])
print(s)
s =all_data_st.groupby("status").agg({"quantity":"sum","quantity":"mean","quantity":"std","unit price":"sum","unit price":"mean","unit price":"std","ext price":"sum","ext price":"mean","ext price":"std"})
print(s)

