
i = 7

if i > 1:
    for j in range(2, i):
        if i % j == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

