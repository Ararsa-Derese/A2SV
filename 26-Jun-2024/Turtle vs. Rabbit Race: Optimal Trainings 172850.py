# Problem: Turtle vs. Rabbit Race: Optimal Trainings - https://codeforces.com/contest/1933/problem/E

import sys, threading
input = sys.stdin.readline
input = lambda: sys.stdin.readline().strip()
from collections import defaultdict
def I():
    return int(input())
def IS():
    return input()
def LI():
    return list(map(int, input().split()))
def MI():
    return map(int, input().split())
def main():
    def cheker():
        i, j = l, n + 1
        while i < j:
            mid = (i + j) // 2
            val = u - (a[mid] - a[l - 1])
            if val <= 0:
                j = mid
            else:
                i = mid + 1
        return j
    t = I()
    for _ in range(t):
        n = I()
        a = [0]+LI()
        for i in range(1, len(a)):
            a[i] += a[i - 1]
        # print(a)
        q = I()
        for _ in range(q):
            l, u = MI()             
            ans = cheker()
            if ans == n + 1:
                ans -= 1
            elif u - (a[ans] - a[l - 1]) < 0:
                s0 = a[ans - 1] - a[l - 1]
                s1 = a[ans] - a[l - 1]
                if s0 * (2 * u - s0 + 1) >= s1 * (2 * u - s1 + 1):
                    ans = max(l, ans - 1)
            print(ans, end=' ')
        print()

 	 	 	  	  		  			  	 			  			
        
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()