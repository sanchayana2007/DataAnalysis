import pandas as pd
import numpy as np
import glob


def add_Steep(group):
	# quantity
	quantity = group.quantity.astype(float)
	#group['MeanDeviation'] = (quantity  - quantity.mean())/quantity.sum()
	group['MeanDeviation'] = group.mad()
	return group

allsales= pd.read_excel("sales-mar-2014.xlsx")
print(allsales.head())
print("INTRODUCED A NEW COLUMN TO SHOW THE QUANTITY PERCENTAGE OF EACH PRODUCTS ON INDIVIDUALs TOTAL ")
print("*********************************************************************************")
allsales=allsales.groupby(['name']).apply(add_Steep)
#allsales=allsales[allsales['name']== 'Barton LLC']
print(allsales.head())
print("**********************************************************************************")
print("SORT ON THE MeanDeviation TO GET THE STEPPEST RISE")
top10 = allsales.sort_values(by=["MeanDeviation"],ascending=False).head()
print(top10.head())
print("**********************************************************************************")
print("SORT ON THE MeanDeviation TO GET THE STEPPEST FALL")
top10 = allsales.sort_values(by=["MeanDeviation"],ascending=True).head()
print(top10.head())
