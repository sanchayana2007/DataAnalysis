import pandas as pd
import numpy as np
import glob


def add_Quantpercenatge(group):
	# quantity
	quantity = group.quantity.astype(float)
	group['Quantpercenatge'] = quantity *100 / quantity.sum()
	return group

def get_quantile_count(group, q=50):
		return group.Quantpercenatge.cumsum().searchsorted(q) 
		

allsales= pd.read_excel("sales-mar-2014.xlsx")
print(allsales.head())
print("INTRODUCED A NEW COLUMN TO SHOW THE QUANTITY PERCENTAGE OF EACH PRODUCTS ON INDIVIDUALs TOTAL ")
print("*********************************************************************************")
allsales=allsales.groupby(['name']).apply(add_Quantpercenatge)
allsales=allsales[allsales['name']== 'Barton LLC']
print(allsales.head())

print("VALIDATE THE SUM OF THE QUANITY PERCENTAGE IS 100 then True ")
print(np.allclose(allsales.groupby(['name']).Quantpercenatge.sum(), 100))
print("**********************************************************************************")

print("SORT THE QUANTITY PERCENTAGE AS DESCENDING FOR TOP 10")
top10 = allsales.groupby(['name']).apply(pd.DataFrame.sort_values,'Quantpercenatge', ascending=False)
print(top10.head())
diversity = top10.groupby(['name']).apply(get_quantile_count)
print(diversity)
