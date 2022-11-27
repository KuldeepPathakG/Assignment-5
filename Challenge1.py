class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self,x,y,z):
        a=x**2
        b=y**2
        c=z**2
        return a+b+c
test1=Point(1,3,5)
print(test1.sqSum(1,3,5))