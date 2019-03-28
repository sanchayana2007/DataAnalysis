library(xlsx)

# Giving the full path 
#PLOT 1
df=read.xlsx("D:/R_DA/sales-jan-2014.xlsx",1,header= T,sep=',')
head(df)

range(df$unit.price)
# Cut the Columns Not needed 
#Only Include the Quantity , price Columns ,ext price
# Find the columns correlations 
M=cor(df[,-c(1,2,3,7,8)]);M
 
#Symbol code to find the correlations distributions 
#using symbol on numbers 
#[1] 0 ' ' 0.3 '.' 0.6 ',' 0.8 '+' 0.9 '*' 0.95 'B' 1
# Values 1 shows perfect corellations and rest symbol are above 
# and 0 no correlation , all other are symbols
symnum(M)

heatmap(M,Rowv = NA,symm = T,col=grey.colors(1000,start = 0.8,end = 0.2))

#Missing values heat map for head record first 6 
heatmap(head(as.matrix(df[,-c(1,2,3,7,8)])),Rowv = NA,Colv = NA,scale = "column",col=grey.colors(1000,start = 0.8,end = 0.2))




      
      