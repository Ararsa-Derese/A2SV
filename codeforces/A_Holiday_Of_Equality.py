n=int(input())
a=list(map(int,input().split()))
mx=max(a)
ans=0
for i in range(n):
    ans+=mx-a[i]
print(ans)