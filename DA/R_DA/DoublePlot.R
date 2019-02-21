library(xlsx)

# Giving the full path 
#PLOT 1
df=read.xlsx("D:/R_DA/sales-jan-2014.xlsx",1,header= T,sep=',')
head(df)


avgprice=c(mean(df[which(df$name=='Barton LLC'),]$ext.price),mean(df[which(df$name=='Kulas Inc'),]$ext.price))
avgprice1=c(mean(df[which(df$name=='BJerde-Hilpert'),]$ext.price),mean(df[which(df$name=='Koepp Ltd'),]$ext.price))
range(avgprice)
barplot(avgprice ,xlab = "",ylab = "",col=c("darkblue","red"))

# Simple Horizontal Bar Plot with Added Labels
box("plot")
legend("topright",inset = 0.005,c("Trans=0"),bty="n",cex=1)
mtext("Avg price",side=2,line = 2.2,cex=0.7,adj = 0)
barplot(avgprice1 ,xlab = "",ylab = "Avg",col=c("darkblue","red"))
box("plot")
mtext("Avg price",side=1,line = 2.2,cex=0.7)
legend("topright",inset = 0.005,c("Trans=1"),bty="n",cex=1)

