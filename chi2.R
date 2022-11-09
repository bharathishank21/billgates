crimedata= matrix(c(162,118,451,18,310,196,996,25,258,193,458,10,280,175,390,19),ncol= 4,byrow =TRUE)

colnames(crimedata)<-c('Assault','Burglary','Larceny','Homicide')
rownames(crimedata)<-c('1','2','3','4')

totalvalue<-sum(crimedata)

rowcrimedata<-c() # each ROW TOTAL
colcrimedata<-c() # each Column Total

for(i in 1:4)
  rowcrimedata[i] = sum(crimedata[i,])

for(i in 1:4)
  colcrimedata[i] = sum(crimedata[,i])

E5<-matrix(ncol = 4,nrow = 4)  #Creating a matrix for expectation  
for(i in 1:4)
{
  for(j in 1:4)
  {
    E5[i,j] = (rowcrimedata[i] * colcrimedata[j])/totalvalue
  }
}

test_stat5<-0
for(i in 1:4)
{
  for(j in 1:4)
  {
    test_stat5 = test_stat5+ (((crimedata[i,j] - E5[i,j])^2)/E5[i,j])      #(Oij - Eij) ^2 / Eij
  }
}

los5<-1
los5<- 1/100

deg5<- ((nrow(crimedata))-1) * ((ncol(crimedata))-1)   #(m-1)(n-1)

value5<-qchisq(los5,deg5,lower.tail = FALSE)

if(test_stat5 <= value5)
{
  print("Null HYP")
}else
  print("Alter Hypo")

