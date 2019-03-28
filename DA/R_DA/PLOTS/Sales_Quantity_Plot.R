library(xlsx)

# Giving the full path 
df=read.xlsx("D:/R_DA/sales-jan-2014.xlsx",1,header= T,sep=',')
head(df)


plot(df$unit.price,df$quantity,las=1,xlab = "Price",ylab = "Quantity",xlim = c(0,200),ylim = c(0,50))

