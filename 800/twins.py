n=int(input())
val=list(map(int,input().split()))
val.sort(reverse=True)
for i in range(0,n):
    if sum(val[:i+1])>sum(val[i+1:]):
        print(len(val[:i+1]))
        break