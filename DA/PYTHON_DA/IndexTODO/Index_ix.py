import pandas as pd
import numpy as np
df = pd.read_excel("excel-comp-data.xlsx")
print(df)
print("Index",df.index)
print("Columns",df.columns)
print("***********************************Setting a Index*********************")
df.set_index('name',inplace = True)
print(df)

print(df.ix["Bauch-Goldner",0])
print("**reate a filter series*********************")
fil = pd.Series([10000,20000],index=["Champlin-Morar","Hahn-Moore"],name="Incr")
print(fil)
print("***********************************Add the filter series*********************")
print(df.Jan + fil)
d =df.Jan + fil

print(d.ix["Champlin-Morar",0])

