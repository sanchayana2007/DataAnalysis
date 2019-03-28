import pandas as pd
import numpy as np
		

allsales= pd.read_excel("sales-mar-2014.xlsx")
print(allsales.head())
allsales.columns = allsales.columns.map(lambda x: x.replace(' ', '_'))
allsales["ext price Check"]=allsales.eval("ext_price /  unit_price")
allsales["ext price Check"] = allsales["ext price Check"].map(lambda x: int(x))
print(allsales.head())
