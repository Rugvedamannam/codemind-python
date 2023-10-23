bs=int(input())
if bs<=10000:
    da=bs*0.8
    hra=bs*0.2
    print("%.2f"%(bs+da+hra))
elif bs<=20000:
    da=bs*0.9
    hra=bs*0.25
    print("%.2f"%(bs+da+hra))
else:
     da=bs*0.95
     hra=bs*0.3
     print("%.2f"%(bs+da+hra))