# n=int(input())
# c=input()
# a=1
# if c[len(c)-1]=="?":
#     a=0
# for _ in range(len(c)-1):
#     if _==0  and c[_]=="?":
#         a=0
#     if _>0 or _<len(c):
#         if c[_]=="?":
#             if c[_+1]==c[_-1]:
#                 a=0
#         if c[_]=="?" and c[_+1]=="?":
#             a=0
#     if c[_]!="?":
#         if(c[_]==c[_+1]):
            
#             a=1
#             break
# if a==1:
#     print("No")
# else:
#     print("Yes")
N = int(input())
s = input()

if ("CC" in s) or ("YY" in s) or ("MM" in s):
    print("No")
elif ("??" in s) or ("C?C" in s) or ("Y?Y" in s) or ("M?M" in s) or (s[0] == "?") or (s[-1] == "?"):
    print("Yes")
else:
    print("No")