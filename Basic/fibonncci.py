a=0
b=1
c=0

print(a)
print(b)
for num in range(7):
    c=a+b
    print(c)
    a=b
    b=c
    num +=1