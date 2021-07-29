# https://codeforces.com/problemset/problem/405/A

n=int(input())
k=list(map(int,input().split()))
k.sort()
for i in range(0,len(k)):
    print(k[i],end=' ')
