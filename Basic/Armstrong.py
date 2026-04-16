n=153
t=n
num=0
while n > 0:
      j=n%10
      num=num + j*j*j
      n=n//10

if num==t:
    print("Armstrong")
else:
    print("not")


n = 153
t = n
num = 0

while n > 0:
    j = n % 10
    num = num + j*j*j
    n = n // 10

if num == t:
    print("Armstrong")
else:
    print("Not Armstrong")