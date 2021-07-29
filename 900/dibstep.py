# https://codeforces.com/problemset/problem/208/A
n=list(map(str,input().split('WUB')))
for i in range(0,n.count('')):
    n.remove('')
print(' '.join(n))

