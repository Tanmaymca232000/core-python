i=56
sum=0
while i>0:
    j=i%10
    sum=sum*10+j
    i=i//10

print(sum)