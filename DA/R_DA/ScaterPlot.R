library(xlsx)

# Giving the full path 
#PLOT 1
df=read.xlsx("D:/R_DA/sales-jan-2014.xlsx",1,header= T,sep=',')
head(df)

#Create Days column from teh Age 
Days=as.Date(df$date) - as.Date("2014-01-01")
Days
graphics.off()
df=cbind(df,Days)
head(df)
str(df)
summary(df)

#ScatterPlot 
# get the Higest and lowest from a Range for finalising the limits 
range(df$Days)
range(df$quantity)

plot(df$quantity,df$Days,xlim = c(-1,80),ylim = c(0,50),xlab = "Quantity",ylab = "Days")

graphics.off()

#We are interested only on the items sold above Quantity 
df=df[df$quantity > 20,]
plot(df$quantity,df$Days,xlim = c(-1,50),ylim = c(0,50),xlab = "Quantity",ylab = "Days")
