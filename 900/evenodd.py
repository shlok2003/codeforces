# https://codeforces.com/problemset/problem/318/A

n=list(map(int,input().split()))

evenpart=n[0]//2
oddpart=n[0]-evenpart

def odd(ind):
    return ind+(ind-1)

def eve(ind,lenoflist,og=True):
    if og==True:
        return ind-(lenoflist-ind)
    else:
        return ind-(lenoflist-ind+1)



if n[1]<=oddpart:
        print(odd(n[1]))
else:
    if evenpart==oddpart:
        print(eve(n[1],n[0]))

    else:
        print(eve(n[1],n[0],False))


