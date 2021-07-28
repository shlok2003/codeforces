# https://codeforces.com/problemset/problem/580/A
n=int(input())
k=list(map(int,input().split()))
maxcount=0
new=0
currcount=0
prevvalue=0
for i in range(0,n):
    if prevvalue<=k[i]:
        currcount+=1
        prevvalue=k[i]
        new=currcount
        if new>maxcount:
            maxcount=new

    else:
        currcount=1
        prevvalue=k[i]
print(maxcount)

    
#     if c<=k[i]:
#         count+=1
#     c=k[i]
# print(count)

# c=2 count=0 
# i=0 count=1 c=2
# i=1 cnt=2 c=2
# i=2 cnt=2 c=9

