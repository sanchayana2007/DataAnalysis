import pandas as pd
import numpy as np

allsales= pd.read_excel("sales-mar-2014.xlsx")
print(allsales.head())
print("INTRODUCED A NEW COLUMN TO SHOW THE QUANTITY PERCENTAGE OF EACH PRODUCTS ON TOTAL ")
print("*********************************************************************************")
alluniqsku= allsales.sku.unique()
#print(dir(allsales))
mask=np.array([i for i in allsales.iterrows() if i['sku']=='B1-20000'])
print(mask)
'''
print("A maskis cretaed a s Filter to Return True or False")
mask=np.array(['B1-50809' in  x  for x in allsales.rows])
print(mask)
allsales=alluniqsku[mask]
print(allsales)
'''




