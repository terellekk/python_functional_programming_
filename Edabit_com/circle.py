class circle:
    def __init__(self, num):
        self.num = float(num)
       
    def getArea(self):
        area = 3.14*self.num*self.num
        return area

    def getPerimeter(self):
        perimeter = 2*3.14*self.num
        return perimeter

attempt1 = circle(11)
print(attempt1.getArea())
print(attempt1.getPerimeter())


