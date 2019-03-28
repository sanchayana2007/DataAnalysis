library(xlsx)


# Giving the full path 
df=read.xlsx("D:/R_DA/sales-jan-2014.xlsx",1,header= T,sep=',')
head(df)

#Apply sam function to diff columns
apply(df[,c[1,2]],MARGIN = 2,FUN = sd)

#Function of useful for repetitive 
#provide the differnce between max , min values for 
mmdiff=function(df){
  apply(df,MARGIN = 2,function(x){max(x)-min(x)})
}

mmdiff(df[,c(5,6)])
