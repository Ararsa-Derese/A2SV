# Problem: A - Large Number - https://codeforces.com/gym/511242/problem/A

from bisect import bisect_left
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = input()
    b=list(a)
    for i in range(len(b)):
        if k > int(b[i]):
            print(''.join(b[:i])+str(k)+''.join(b[i:]))
            break
    else:
        print(a+str(k))