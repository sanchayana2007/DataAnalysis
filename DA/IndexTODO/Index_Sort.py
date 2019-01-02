import pandas as pd
import numpy as np
df = pd.read_excel("excel-comp-data.xlsx")
df =df.sort_values('Jan', ascending=False)[:10]
print(df)
print("Series of JAN")
print(df["Jan"])
print("************************DIVIDE THE SERIES IN PERCENTAGES**********************************************")
print("50 percentage value in te series")
print(df["Jan"].quantile(0.5))
print("************************************************************************************")
print("50 percentage value in te series")
print(df["Jan"].quantile())
print("************************************************************************************")
print("20 percentage value in te series")
print(df["Jan"].quantile(0.2))
print(df["Jan"].sem())

