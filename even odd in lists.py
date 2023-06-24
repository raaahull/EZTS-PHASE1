Lst=[1,4,5,7,10,15,45,99,20]
odd=[]
even=[]
for i in Lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print("odd",odd)
print("even ",even)
    
