library(xlsx)


# Giving the full path 
df=read.xlsx("D:/R_DA/sales-jan-2014.xlsx",1,header= T,sep=',')
head(df)

df=df[,!apply(is.na(df), 2, all)]
#To get the Idea of Mean ,Median ,counts 
summary(df)

countinvalid=function(x)sum(x=="-1")
#dfsum=data.frame(average=sapply(df[,-1],mean),Median=sapply(),median,countblank)

#Corelation 
M=cor(df[,-c(1,2,3,7,8)]);M

#for age groups 
for (x in df$quantity)
{
  c_quantity=c(Ext_price,100 * sum(df$unit.price==x & df$ext.price==0)/sum(df$quantity==x))
}