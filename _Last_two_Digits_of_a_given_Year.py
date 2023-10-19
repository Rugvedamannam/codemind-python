n=int(input())
s=n%100
s=str(s)
if(len(s)==2):
    print(s)
else:
    print("0"+s)