L=[1,2,3,5,6]
L[0:3]
print(L)
L=['v' ,'e', 'r', 'y', 'g', 'o', 'o', 'd', 'd', 'a', 'y']
L[4:8]
print(L[4:8])


L=["hyd","vizag","chennai","vijaywada"]
city=[]
for n in L:
    if "v" in n:
        city.append(n)
print(city)

L1=[2**x for x in range(2,10)]
print(L1)

L2=[a for a in range(100,201,20)]
print(L2)

L3=[1,2,3,4,5,6]
L4=[i for i in L3 if (i<5)]
print(L4)
