import pandas as pd
import numpy as np
import glob

data= []
print("*******************************MERGE 2 FILES AND CONCATE IN DF*************************")
for f in glob.glob("sales*.xlsx"):
	df = pd.read_excel(f)
	print("Len of Single Excel",len(df.index))
	data.append(df)
print("Len of data",len(data))

allsales= pd.concat(data,ignore_index=True)
print(allsales.head())
print("Shape of Total",allsales.shape)
print("Len of Total",len(allsales.index))
print("**********************************************************************************")
