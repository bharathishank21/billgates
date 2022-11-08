c1<-c(551,457,450,731,499,632)
c2<-c(595,580,508,583,633,517)
c3<-c(639,615,511,573,648,677)
c4<-c(417,449,517,438,415,555)
c5<-c(563,631,522,613,656,679)

data<-data.frame(cbind(c1,c2,c3,c4,c5))
summary(data)

stacked<-stack(data)
stacked

result<-aov(values~ind,data=stacked)
summary(result)


hist(result$residuals)

qf(1-0.05,4,25)
if(result<=qf)
{
  print("NULL HYPOHESIS")
}
else
{
  print("ALTERNATE HYPOTHESIS")
}