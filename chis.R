x<-c(31,24,34,39,36,31,36,35,40,44)
y<-c(35,35,35,35,35,35,35,35,35,35)

num=length(x)
test_sta=0
for(i in 1:10)
{
  test_sta=test_sta+(((x[i]-y[i])^2)/y[i])
}

test_sta
deg=num-1
los=readline()
los=strtoi(los)
los=los/100
value=qchisq(los,deg,lower.tail=FALSE)
value
if(test_sta<=value)
{
  print("NULL HYPOTHESIS")
}else
{
  print("ALTERNATE HYPOTHESIS")
}