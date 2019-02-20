library(xlsx)

# Giving the full path 
#PLOT 1
df=read.xlsx("D:/R_DA/sales-jan-2014.xlsx",1,header= T,sep=',')
head(df)

range(df$unit.price)
#hist(df$quantity,xlim = c(-5,30),ylim = c(0,110),xlab = "MEDV")
graphics.off()

boxplot(df$ext.price~ df$quantity,ylim=c(0,15),xlab="Price",ylab="Quantity")