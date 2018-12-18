import pandas as pd
import numpy as np
df = pd.read_excel("excel-comp-data.xlsx")
print(df.head())
print("TOTAL ROWS AND PALCE IN NEW COLUMN")
df["total"] = df["Jan"] + df["Feb"] + df["Mar"]
print(df.head())
print(df["Jan"].sum())
#print(df["Jan"].sum(), df["Jan"].mean(),df["Jan"].min(),df["Jan"].max())
df_sum=pd.DataFrame(data=sum_row).T
print(df_sum)

