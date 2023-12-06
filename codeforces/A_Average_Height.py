t=int(input())
for _ in range(t):
    c=int(input())
    a=list(map(int,input().split()))
    o=[]
    e=[]
    for i in range(c):
        if a[i]%2==0:
            e.append(a[i])
            
        else:
             o.append(a[i])

    o.extend(e)
    print(*o)
    