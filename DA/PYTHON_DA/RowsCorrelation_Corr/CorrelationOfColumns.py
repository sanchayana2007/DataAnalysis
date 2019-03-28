import numpy as np
import pandas as pd

BOEDb= pd.read_excel("Bank of England  Database.xlsx")
#BOEDb=BOEDb.rename(columns={BOEDb.columns[0]:"OutStanding Govt Holdings",BOEDb.columns[1]:"OutStanding Savings",BOEDb.columns[2]:"certificates of tax deposit"})
print(BOEDb.head())
BOEDb.fillna(0,inplace=True)
print(BOEDb.head())
t= BOEDb[' conventional gilts '].corr(BOEDb[' national savings'])
print("Correlation is ",t)
if t >0.5:
	print("Columns have some corelation")
else:
	print("Columns have NO  corelation")
