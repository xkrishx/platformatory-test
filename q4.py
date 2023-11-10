class Vector:
    def __init__(self, x, y):
        self.x= x
        self.y= y

    def add(self, vec2):
        sumx= self.x + vec2.x
        sumy= self.y + vec2.y

        newvector=Vector(sumx, sumy)
        print(newvector.x, newvector.y)

a=Vector(2,3)
b=Vector(5,6)

c=a.add(b)