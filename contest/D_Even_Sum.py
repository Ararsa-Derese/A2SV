# n=int(input())
# a=list(map(int,input().split()))
# o=[]
# e=[]
# ans=0
# for i in range(n):
#     if a[i]%2==0:
#         e.append(a[i])
#     else:
#         o.append(a[i])
# o.sort(reverse=True)
# if len(o)%2==0:
#     for j in range(0,len(o),2):
#         ans+=(o[j]+o[j+1])
# else:
#     for k in range(0,len(o)-1,2):
#         ans+=(o[k]+o[k+1])
# for l in range(len(e)):
#     ans+=e[l]
# print(ans)
N = int(input())
nums = list(map(int, input().split()))
total = sum(nums)
if total % 2 == 0:
    print(total)
else:
    min_odd = float('inf')
    for num in nums:
        if num % 2 == 1:
            min_odd = min(min_odd, num)
    print(total - min_odd)