n,m,c=map(int,input().split())
s=(n+m+c)/2
a=(s*(s-n)*(s-m)*(s-c))**0.5
print('%.2f'%(a))