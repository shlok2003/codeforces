# https://codeforces.com/problemset/problem/96/A

n=input()
sample1,sample2='0000000','1111111'
x=n.find(sample1)
y=n.find(sample2)
if x==-1 and y==-1:
    print('NO')
else:
    print('YES')