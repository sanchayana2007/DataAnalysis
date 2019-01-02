#Data Source :http://www.grouplens.org/node/73 
import pandas as pd  # first time it loades cache it will take some time to Run it 
import numpy as np # first time it loades cache it will take some time to Run it 
import os.path # To check if Src data files are there or not 

if __name__=="__main__":

	df = pd.read_excel("sales-funnel.xlsx")
	print(df.head())
	print("PIVOT TABLE: TOTAL SUMS OF REP UNDER MANAGERS")
	normalpivot = pd.pivot_table(df,index=["Manager","Rep"],values=["Price"],aggfunc=[np.sum],margins=True)
	print(normalpivot)
	summean=pd.pivot_table(df,index=["Manager","Rep"],values=["Price","Quantity"],aggfunc=[np.sum,np.mean])
	print("PIVOT TABLE: TOTAL SUMS , MEAN")
	print(summean)
	=pd.pivot_table(df,index=["Manager","Rep"],columns=["Product"],values=["Price"],aggfunc=[np.sum]	

