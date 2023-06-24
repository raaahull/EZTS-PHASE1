'''1. __del__()-deletes the scope autom..
2. __repr__()-string represntation..
3. __cmp__()-compares two class objects..
4. __len__()-length of a class objects..
5. __call__()-the method lets a class to act like a function
6. __lt__, __le__, __eq__, __ne__, __gt__, __ge__ these are used to compare 2 object
7. __hash__-=it is used to hash the objects
8. __iter__-- itenrates over the object
9.__getitem__- used for indexing
10.def __getitem__()
__setitem__()
def __setitem__ (self, key,  value)'''


def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,c,b)
        if a:
            c.append(a.pop())
        hanoi(n-1,b,a,c)
a=[1,2,3,4]
b=[]
c=[]
hanoi(len(a),a,b,c)
print(a,b,c)
