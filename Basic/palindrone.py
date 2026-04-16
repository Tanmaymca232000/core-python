n=151
num=0
t=n
while n != 0:
 j=n%10
 num=num*10+j
 n=n//10

if t==num:
    print("palinmdrone")
else:
    print("not")
