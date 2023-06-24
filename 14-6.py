'''the constant pi=3.14159 use the class variable to calculate area nd
circumfurance in different functions witha specific radius 7.5 '''
class circle:
    pi=3.14159
    def area(self,r):
        n=self.pi
        a=n*(r**2)
        print(a)
    def circumference(self,r):
        l=self.pi
        c=2*l*r
        print(c)
obj=circle()
obj.area(6)
obj.circumference(2)

