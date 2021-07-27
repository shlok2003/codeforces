n=int(input())
p=list(map(int,input().split()))
count=0
for i in range(0,len(p)):
    count+=p[i]/100
print((count/n)*100)

