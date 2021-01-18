
n='123456789'
a=12
s=0
while len(str(a))<=9:
    p=True
    for x in range(len(str(a))):
        if not n[x] in str(a):
            p=False
            break
    if p:
        b=2
        q = True
        while a>=b*b:
            if a%b==0:
                q=False
                break
            b += 1
        if q:
            s=a
            print(s)
    a += 1
print(s)
