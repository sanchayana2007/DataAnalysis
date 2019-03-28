import pandas as pd 
  
#reading csv files 
pokemon_names = pd.read_excel("sales-feb-2014.xlsx", usecols = ["account number"], 
                                                  squeeze = True) 
  
#usecol is used to use selected columns 
#index_col is used to make passed column as index 
pokemon_types = pd.read_excel("customer-status.xlsx", index_col = "account number", 
                                                  squeeze = True) 
  
#using pandas map function 
new=pokemon_names.map(pokemon_types) 
  
print (new) 
