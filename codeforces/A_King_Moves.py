a=input()
if a[0]=='a' or a[0]=='h':
    if a[1]=='1' or a[1]=='8':
        print(3)
    else:
        print(5)
elif a[1]=='1' or a[1]=='8':
    if a[0]=='a' or a[0]=='h':
        print(3)
    else:
        print(5)
else:
    print(8)