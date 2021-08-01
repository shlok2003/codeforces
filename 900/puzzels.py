# https://codeforces.com/problemset/problem/337/A

n=list(map(int,input().split()))
k=list(map(int,input().split()))
k.sort()
m=1000
d=0
for i in range(n[1]-n[0]+1):
   d=k[i+n[0]-1]-k[i]
   if d<m:
      m=d
print(m)