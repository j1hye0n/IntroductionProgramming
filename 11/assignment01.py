class Rectangle :
    shape_type = "Rectangle"
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self) :
        return (self.width*self.height)
    
    def perimeter(self) :
        return (self.width+self.height)*2
    
    def is_square(self) :
        return True if self.width==self.height else False