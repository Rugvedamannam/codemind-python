x=int(input())
a=0
b=0
b=x//10
x-=b*10
a=x//5
x-=a*5
if x==0:
    c=a+b
    print(c)
else:
    print("-1")