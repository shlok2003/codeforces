# https://codeforces.com/problemset/problem/133/A

n=input()
sample='HQ9'
c=0
for i in range(0,len(n)):
    if n[i] in sample:
        c+=1
if c>0:
    print('YES')
else:
    print('NO')
    