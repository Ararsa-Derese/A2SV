# Problem: B - Yikes! - https://codeforces.com/gym/511242/problem/B

from bisect import bisect_left, bisect_right
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

c = [1, a[0]] 
x , y = 1, a[0]
for i in range(n-1):
    c.append(x+a[i])
    c.append(y+a[i+1])
    x = c[-2]
    y = c[-1]
for i in range(m):
    print((bisect_right(c, b[i])+1)//2)
    