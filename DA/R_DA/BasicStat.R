library(xlsx)


# Giving the full path 
df=read.xlsx("D:/R_DA/sales-jan-2014.xlsx",1,header= T,sep=',')
head(df)

#To get the Idea of Mean ,Median ,counts 
summary(df)


#Correlation 
# Shows the relation between two columns 
# Close to 0 Shows less  relation 
#Close to 1 shows more relation .
cor(df$unit.price,df$quantity)


#Covariance shows spread of values and intersection between 
#this 2 regions 
cov(df$unit.price,df$ext.price)

#Mean 
mean(df$unit.price)
median(df$unit.price)

#IQR : Interquartile range Difference between 1st and 3rd Quarter 
IQR(df$unit.price)


#Standard Deviation 
sd(df$unit.price)

#Variance
var(df$unit.price)

#Apply sam function to diff columns
apply(df[,c[1,2]],MARGIN = 2,FUN = sd)

#Function of useful for repetitive 
#provide the differnce between max , min values for 
mmdiff=function(df){
  apply(df,MARGIN = 2,function(x){max(x)-min(x)})
}

mmdiff(df[,c(5,6)])


