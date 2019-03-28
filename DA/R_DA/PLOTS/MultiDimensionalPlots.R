library(xlsx)

# Giving the full path 
#PLOT 1
df=read.xlsx("D:/R_DA/sales-jan-2014.xlsx",1,header= T,sep=',')
head(df)

#Multidimesional Visualisation Plots using 
#color coded Plots 
Days=as.Date(df$date) - as.Date("2014-01-01")
Days
palette(rainbow(6))
df=cbind(df,Days)

# The 3rd Dimesion will be shown by Colour 
# Theere are 6-7 colours to show a factor column readings over ploted x and y columns
#
plot(df$quantity,df$Days,xlim = c(-1,50),ylim = c(0,50),xlab = "Quantity",ylab = "Days",col=df$Days)
