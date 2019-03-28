library(xlsx)

# Giving the full path 
#PLOT 1
df=read.xlsx("D:/R_DA/sales-jan-2014.xlsx",1,header= T,sep=',')
head(df)


tsv=ts(df$quantity,start=c(1,1),end=c(28,1),frequency = 15)
plot(tsv,xlab = "January",ylab = "Quantity",las=2)



#PLOT 2

#This section provide Formating of the above plot 
atl=seq(as.Date("2014-01-01"),as.Date("2014-01-28"),by="1 year")
alabels1=format(atl,"%D") # Format the ate string creating labels
par(mar=c(8,4,4,1)+0.1)

plot(tsv,xlab="",ylab="",xaxt="n",yaxt="n")
axis(1,las=2)
axis(2,las=2)
mtext(side=1,text = "2014",line = 5.5)
mtext(side = 2,text = "Quantity",line = 3.0)

#close all graphics 
graphics.off()
 