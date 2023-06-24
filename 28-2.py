#1+1/2+.....1/(n) find the 5th term
'''n=int(input("enter the term:"))
s=0.0
for i in range(1,n+1):
    a=1.0/i
    s+=a
print(s)'''



'''n=int(input("enter the term:"))
while n>=0:
    print(n, end=" ")
    n-=1'''

#Strong num
sum=0
n=int(input("enter the number:"))
temp=num
while (num):
    i=1
    fact=1
    remainder=num%10
    while(i<=remainder):
        fact=fact*i
        i=i+1
        sum=sum+fact
        num=num//10
if (sum==temp):
    print("is a strong number")
else:
    print("is not a strong number")

