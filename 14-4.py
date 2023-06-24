class number :
    even=0
    def check(slef,num):
        if num%2==0:
            self.even=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num, "is even")
        else:
            print(num, "is odd")
n=number()
n.even_odd(99)
