from bisect import bisect_right
n = int(input())
a = list(map(int,input().split()))
a.sort()
x = int(input())
for _ in range(x):
    print(bisect_right(a,int(input())))