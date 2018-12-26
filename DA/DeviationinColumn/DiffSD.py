import pandas as pd
import numpy as np


Jansales = pd.read_excel("sales-jan-2014.xlsx")
Febsales = pd.read_excel("sales-feb-2014.xlsx")
print(Jansales.head())
print(Febsales.head())
sum_Jan=pd.pivot_table(Jansales,index=["name"],values=["quantity"],aggfunc=[np.sum])
sum_Feb=pd.pivot_table(Febsales,index=["name"],values=["quantity"],aggfunc=[np.sum])
print(sum_Jan.head())
print(sum_Feb.head())

diff=sum_Jan['sum'] - sum_Feb['sum']
print("*************************************DIFFRENCE IN SALES")
sorted_by_diff = diff.sort_values(by=["quantity"])
print(sorted_by_diff.head())
jansd=Jansales.groupby('name')['unit price'].std()
print("STD ON UNITPRICE PER PRODUCT ********************************")
jansd=jansd.sort_values(ascending=False)
print(jansd)
