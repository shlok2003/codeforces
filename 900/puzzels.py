# https://codeforces.com/problemset/problem/337/A

n=list(map(int,input().split()))
k=list(map(int,input().split()))
k.sort()
m=1000
d=0
for i in range(n[1]-n[0]+1):
     l=k[i:n[0]-i+1]
     if l==n[0]:
        d=abs(l[n[0]-i+1]-l[i])
     if d<m:
         m=d
print(m)