library(xlsx)


# Giving the full path 
df=read.xlsx("D:/R_DA/sales-jan-2014.xlsx",1,header= T,sep=',')
#Storing different data types 
is.data.frame(df);df
df$account.number
length(df$account.number)
is.vector(df$account.number)
#is a categorical variable As account should return as False
is.factor(df$account.number) #FALSE
is.factor(df$name) #TRUE

#Structure of data frame is like a desc s
str(df)
typeof(df)

#Subsetting the operator 
df[,3]#get the 3rd column
df[1:5,]# get the first 5 rows 
df[,c(1,3)] # the 1st 3 columns 

df[df$quantity > 200]


head(df$account.number)

#Creatinga Account Number Gropus usinga vector 
acno_charcter=vector(mode="character",length=length(df$account.number))
acno_charcter[df$account.number > 500000]="Higher Account Number"
acno_charcter[df$account.number < 500000]="Lower Account Number"
acno_charcter
#Creatinga factor or GROUPBY varibale form the list 
acno_class=factor(acno_charcter,c("Higher Account Number","Lower Account Number"),ordered = T)
#We need to bind this columns with the Orig data columns 
df=cbind(df,acno_class)
str(df)


#Contigency Tables 
# To count the GROUPBY/factor items found
ct=table(df$account.number,df$acno_class);ct
class(ct)
dim(ct)


