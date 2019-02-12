library(xlsx)

df=read.xlsx(file.choose(),1,header=T)
# Giving the full path 
df=read.xlsx("D:\R_DA\sales-jan-2014.xlsx",1,header= T,sep=',')


#Set the Working Dir and then mention the data set path 
setwd('D:/R_DA/')
df1=read.xlsx("sales-jan-2014.xlsx",1,header= T)

#Create diff data types 
i =1 #int 
country = "INDIA" # String 
flag=T # Logical 

#Find the data types of a vaible
class(i)
typeof(country)

#Check the type and Changethe type
j=1.5
j=as.integer(j):j
is.integer(j)
  
#length of the variabe
length(i)

#Vectors are Arrays : List 
is.vector(j)
#create and Print 
v=c("cricket","Badmington","Football");v
v[1]

#Sum up a series 
v1=1:3;v1

v2=v1*2;v2
v2[3];v1;v2
# all the values greater then 8 
v3=v2+v1;v3
v3[v3>8 | v3 < 5]

#Intialise and then populate vector 
v4=vector(length= 4);v4
#create a numeric vector 
v5=vector(mode="integer", length = 4);v5

#Array and matrices 
A=array(0,dim=c(3,3,2))
A[2,2,2]=1000;A

#A 2d array matrix 
#matrix() function 
M= matrix(0,nrow=3,ncol=3);M
M1=matrix(c(1,23,4,5,43,98),nrow = 3,ncol = 2);M1
#multiple yhe matrix 
M1 %*% M1

#Inverse of a Suqare Matrix Only 
library(matrixcalc)
matrix.inverse(M1)

#Transpose 
t(M1)

