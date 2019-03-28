library(xlsx)


# Giving the full path 
df=read.xlsx("D:/R_DA/sales-jan-2014.xlsx",1,header= T,sep=',')
head(df)
x1=rnorm(20,mean = 50,sd=5)
y1=rnorm(20,mean = 60,sd=5)


#Students t-test
t.test(x1,y1,var.equal = T)
#t-value for 2 sided hypothesis test at 0.05 significance level
qt(p=0.05/2,df=20+30-2,lower.tail = F)

#welch test 
t.test(x1,y1,var.equal = F)
