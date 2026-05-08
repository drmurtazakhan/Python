l1 = [2, 3, 4, 5, 7, 9, 10, 11, 12, 13, 14]
print(l1)
for i in range(len(l1)):
    flag = False
    to = int(l1[i]/2)
    for j in range(2, to+1):
        if (l1[i]%j == 0):
            flag = True
            break
    if flag:
        print(str(l1[i])+" is not prime")
    else:
        print(str(l1[i])+" is prime")
