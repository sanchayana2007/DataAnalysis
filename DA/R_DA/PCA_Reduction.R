library(xlsx)


# Giving the full path 
df=read.xlsx("D:/R_DA/nics-firearm-background-checks.xlsx",1,header= T,sep=',')
head(df)
df1=df1[,!apply(is.na(df1),2,all)]
df1[1:20,]

str(df1)
df2=as.data.frame(lapply(df[,-c(1,2,24)],function(x){x=100*x/df$handgun}))
