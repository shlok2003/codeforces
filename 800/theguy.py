n=int(input())
sample=set(range(1,n+1))
x=list(map(int,input().split()))
y=list(map(int,input().split()))
new=set(x[1:]+y[1:])
if sample == new:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')