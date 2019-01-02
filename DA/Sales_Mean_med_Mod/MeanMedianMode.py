import pandas as pd
import numpy as np


Jansales = pd.read_excel("sales-jan-2014.xlsx")
print(Jansales.head())

print("Mode",Jansales['quantity'].mode())

print("*************************************DIFFRENCE IN SALES")
#jansd=Jansales[Jansales['name']=='Barton LLC']
jansd=Jansales[Jansales['name']=='Kulas Inc']
print(jansd)
#jansd=Jansales.groupby('name')['quantity'].median()
print("Median",jansd['unit price'].median())
print("Mean",jansd['unit price'].mean())
