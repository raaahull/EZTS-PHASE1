L2=[a for a in range(150,181)]
print(L2)
L1=[i for i in L2 if(i%2==0)]
L3=[i for i in L2 if(i%2!=0)]
print(L1)
print(L3)

L2=[a for a in range(1,11)]
L1=["even" if i%2==0 else "odd" for i in L2]
print(L1)




