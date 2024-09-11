# Problem: C - Spaceship Attack - https://codeforces.com/gym/511242/problem/C

from bisect import bisect_right
s, b = map(int, input().split())
a = list(map(int, input().split()))
c = []
for _ in range(b):  
    c.append(list(map(int, input().split())))
c.sort(key=lambda x: x[0])

d = [i[0] for i in c]
d.sort()
ps = [0]*b
ps[0] = c[0][1]
for i in range(1, b):
    ps[i] = ps[i-1]+c[i][1]
for i in range(s):
    if bisect_right(d, a[i])-1 < 0:
        print(0, end=' ',)
    else:
        print(ps[bisect_right(d, a[i])-1], end=' ',)