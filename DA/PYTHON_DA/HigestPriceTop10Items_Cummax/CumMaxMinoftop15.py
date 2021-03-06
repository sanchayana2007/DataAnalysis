import pandas as pd
import numpy as np


def add_Quantpercenatge_Sum(group):
	productsum = group.quantity.astype(float)
	group['totalQuantpercenatge'] = productsum.sum() *100 / total
	return group 
		

allsales= pd.read_excel("sales-mar-2014.xlsx")
print(allsales.head())
total= allsales['quantity'].sum()
print("INTRODUCED A NEW COLUMN TO SHOW THE QUANTITY PERCENTAGE OF EACH PRODUCTS ON TOTAL ")
print("Total sold items number",total)
print("*********************************************************************************")
#allsales= allsales.groupby(['name']).agg({"quantity":"sum"})
#print(allsales.head())
allsales=allsales.groupby(['name']).apply(add_Quantpercenatge_Sum)
print("Percenntage of Item Quantity with total Sold")
print(allsales.head())
print(np.allclose(allsales.totalQuantpercenatge.sum(), 100))
t = allsales.sort_values(by='totalQuantpercenatge', ascending=False)
print(t[:15])
t['Running Max']= t['unit price'].cummax()
print("INTRODUCED A NEW COL TO SHOW THE RUNNING MAX in the Top 15 : SOLD QUANTITY PRODUCT")
print("*********************************************************************************")
t['Running Min']= t['unit price'].cummin()
print("INTRODUCED A NEW COL TO SHOW THE RUNNING MIN in the Top 15 : SOLD QUANTITY PRODUCT")
print("*********************************************************************************")
print(t[:15])

