# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

m, s = map(int, input().split())
if s == 0:
    if m == 1:
        print("0 0")
        exit()
    else:
        print("-1 -1")
        exit()

if s > 9 * m:
    print("-1 -1")
    exit()
mn = [0] * m
sm = s

for i in range(m):
    for digit in range(10):
        if (i > 0 or digit > 0 or (m == 1 and digit == 0)) and (sm - digit >= 0) and (sm - digit <= 9 * (m - i - 1)):
            mn[i] = digit
            sm -= digit
            break

max_number = [0] * m
sm = s

for i in range(m):
    for digit in range(9, -1, -1):
        if (i > 0 or digit > 0 or (m == 1 and digit == 0)) and (sm - digit >= 0) and (sm - digit <= 9 * (m - i - 1)):
            max_number[i] = digit
            sm -= digit
            break

print("".join(map(str, mn)) + " " + "".join(map(str, max_number)))