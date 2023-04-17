r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
m=0
for i in range(r):
    for j in range(c):
        m+=mat[i][j]
print(m)