car = table(c(1,2,3,4),c(10,20,30,40))
print(car)
# Perform the Chi-Square test.
test_sta=chisq.test(car)
test_sta
def=chisq.test(car)[2]
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