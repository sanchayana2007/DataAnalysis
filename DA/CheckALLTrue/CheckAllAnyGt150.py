import pandas as pd
import numpy as np
import glob


def add_TrueQuantityGt150(group):
	# quantity
	quantity = group.quantity.astype(int)
	if quantity.sum() > 150:
		group['QuantityGt150'] = True
		group['QSum'] = quantity.sum()
	else:
		group['QuantityGt150'] = False
		group['QSum'] = quantity.sum()
	return group

		

print("*********************************************************************************")
allsales= pd.read_excel("sales-mar-2014.xlsx")
print(allsales.head())
allsales['quantity'].replace(to_replace=-1,value=0,inplace=True) 
print(allsales.head())
print("INTRODUCED 2 NEW COLUMNs TO SHOW THE QUANTITY Sum And Quantity gt 150")
print("*********************************************************************************")
allsales=allsales.groupby(['name'],sort=True).apply(add_TrueQuantityGt150)
print(allsales.head())
print("All Values in QuantityGt150 are True ",allsales['QuantityGt150'].all())
print("Any of the Values in QuantityGt150 are True",allsales['QuantityGt150'].any())
