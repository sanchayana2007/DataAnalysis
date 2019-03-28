library(xlsx)

# Giving the full path 
#PLOT 1
df=read.xlsx("D:/R_DA/sales-jan-2014.xlsx",1,header= T,sep=',')
head(df)


avgprice=c(mean(df[which(df$name=='Barton LLC'),]$ext.price),mean(df[which(df$name=='Kulas Inc'),]$ext.price))
range(avgprice)
barplot(avgprice ,xlab = "Cust name",ylab = "Avg",ylim = c(0,1400),col=c("darkblue","red"),legend = rownames(avgprice), beside=TRUE)
t=c("Barton LLC","Kulas Inc")
# Simple Horizontal Bar Plot with Added Labels


