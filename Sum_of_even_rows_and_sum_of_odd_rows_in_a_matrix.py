r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
m=0
s=0
for i in range(r):
        if(i%2==0):
             for j in range(c):
              s+=mat[i][j]
        else:
             for j in range(c):
                m+=mat[i][j]
print(s,m)
        