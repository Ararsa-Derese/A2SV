t=int(input())
for _ in range(t):
    s=int(input())
    a=list(map(int,input().split()))
    for i in range(s):
        if a.count(a[i])==1:
            print(i+1)
            break