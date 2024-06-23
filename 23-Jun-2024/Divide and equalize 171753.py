# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

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
    def fact(i):
        curr = i
        div = 2
        while div*div <= curr:
            while curr % div == 0:
                curr //= div
                dictn[div] += 1
            div += 1
        if curr > 1:
            dictn[curr] += 1
    t = I()
    for _ in range(t):
        n = I()
        a = LI()
        dictn = defaultdict(int)
        for i in a:
            fact(i)
        for key in dictn.keys():
            if dictn[key] % n != 0:
                print("NO")
                break
        else:
            print("YES")
            


            
        
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()