
dist1 = 305106211101695


count1 = 0


tabtest1 = []

for i in range(0,45977295+1):
    tabtest1.append(i)
for j in range(0,45977295+1):
    if tabtest1[j]*tabtest1[-j-1]>dist1:
        count1+=1
print(count1)


