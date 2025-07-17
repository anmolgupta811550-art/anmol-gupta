lst = [7,3,5,3,6,4,1]
profit = 0
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if(lst[j]-lst[i]>profit):
            profit = lst[j] - lst[i]

print(profit)