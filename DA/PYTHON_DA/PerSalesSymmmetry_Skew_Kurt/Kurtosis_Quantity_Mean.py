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
top10["Quantity kurt"] = allsales["quantity"].kurt()
top10["Mean kurt"] = allsales["Mean"].kurt()
top10["Fisher kurtosis"] = allsales["Mean"].kurtosis()
print(top10.tail())
print("********************BELL CURVE ANALYSIS *********************************")
t = top10
if t["Quantity kurt"].between(0,0.5).all():
	print("Quantity Kurtosis  0")
	print("The Quantity Distribution is SMOOTH  to Bell Curve")
elif (t["Quantity kurt"] > 0.5).all():
	print("Quantity is Kurtosis Positive")
	print("The Distribution Bell Curve is Flat ")
elif (t["Quantity kurt"] < 0).all():
	print("Quantity is Kurtosis Negatively: Assemetric")
	print("The distribution Bell Curve is Pointed ")

if t["Mean kurt"].between(0,0.5).all():
	print("Mean is Kurtosis Near 0")
	print("The Mean Distribution is SMOOTH  to the mean")
elif (t["Mean kurt"] > 0.5).all():
	print("Mean is Kurtosis Positive")
	print("The Distribution Bell Curve is Flat ")
elif (t["Mean kurt"] < 0).all():
	print("Mean is Kurtosis Negatively: Assemetric")
	print("The distribution Bell Curve is Pointed ")

