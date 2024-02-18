t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    s=list(s)
    
    dic={}
    sum=1
    dic[sum]=1
    ans=0
    for i in range(1,n+1):
        sum+=int(s[i-1])
        if sum-i in dic:
            ans+=dic[sum-i]
        if sum-i in dic:
            dic[sum-i]+=1
        else:
            dic[sum-i]=1
    print(ans)
    