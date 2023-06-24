'''n1=number(21)
n2=number(32)
n3=number(43)
n4=number(54)
n5=number(65)'''
'''output:
            even numbers are : [32, 54]
            odd numbers are : [21,43,65]'''
class number:
    evens= []
    odds= []
    def __init__(self,num):
        self.num = num
        if num%2==0:
            number.evens.append(num)
        else:
            number.odds.append(num)
n1=number(21)
n2=number(32)
n3=number(43)
n4=number(54)
n5=number(65)
print("even numbers are :",number.evens)
print("odd numbers are :",number.odds)
