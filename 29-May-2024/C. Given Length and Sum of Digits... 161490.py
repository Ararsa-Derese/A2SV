# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

import sys
m,s = map(int,sys.stdin.readline().strip().split())
if 9 * m <s:
    print(-1,-1)
elif s == 0 :
    if m !=1:
        print(-1,-1)
    else:
        print(0,0)
else:
    minim = [0] * m
    maxim = [0] * m
    i = 0
    temp_s = s
    while i < len(maxim):
        maxim[i] = min(temp_s,9)
        temp_s -= min(temp_s,9)
        if temp_s <= 0:
            break
        i+=1
    temp_s = s
    #print(minim)
    minim[0] = 1
    temp_s -= 1
    i = len(minim)-1
    while i > -1:
        minim[i] += min(temp_s,9)
        temp_s -= min(temp_s,9)
        if temp_s <= 0:
            break
        i-=1
    
    print(int("".join(map(str,minim))),int(int("".join(map(str,maxim)))))
