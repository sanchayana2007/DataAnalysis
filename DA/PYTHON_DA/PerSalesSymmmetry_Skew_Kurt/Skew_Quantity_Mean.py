import pandas as pd
import numpy as np
import glob


def add_Steep(group):
	# quantity
	quantity = group.quantity.astype(float)
	group['Mean'] = quantity.mean()
	return group

allsales= pd.read_excel("sales-mar-2014.xlsx")
print(allsales.head())
print("INTRODUCED A NEW COLUMN TO SHOW THE QUANTITY PERCENTAGE OF EACH PRODUCTS ON INDIVIDUALs TOTAL ")
print("*********************************************************************************")
allsales=allsales.groupby(['name']).apply(add_Steep)
#allsales=allsales[allsales['name']== 'Barton LLC']
print(allsales.head())
print("**********************************************************************************")
top10 = allsales
top10["Quantity skew"] = allsales["quantity"].skew()
top10["Mean skew"] = allsales["Mean"].skew()
print(top10.tail())
print("******************************DISTRIBUTION VOLUME ANALYSIS : SKEW*************************************")
t = top10
if t["Quantity skew"].between(0,0.5).all():
	print("Quantity is Skewed Near 0")
	print("The Quantity Distribution is Symetric to the mean")
elif (t["Quantity skew"] > 0.5).all():
	print("Quantity is Skewed Positively: Assemetric")
	print("The Quantity Distribution is More After Mean")
elif (t["Quantity skew"] < 0).all():
	print("Quantity is Skewed Negatively: Assemetric")
	print("The Quantity Distribution is More before Mean")

if t["Mean skew"].between(0,0.5).all():
	print("Mean is Skewed Near 0")
	print("The Mean Distribution is Symetric to the mean")
elif (t["Mean skew"] > 0.5).all():
	print("Mean is Skewed Positively: Assemetric")
	print("The Mean Distribution is More After Mean")
elif (t["Mean skew"] < 0).all():
	print("Mean is Skewed Negatively: Assemetric")
	print("The mean Distribution is More before Mean")

