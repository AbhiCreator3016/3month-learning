class CreatePoint:
    def __init__(self,x,y):
        self.x=x;
        self.y=y;
        
    def __str__(self):
        return (f"X : {self.x} | Y : {self.y}")

    def distance(self,other):
        return(((self.x - other.x)**2 + (self.y - other.y)**2)**0.5)
    
class CreateLine:

    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
    
    def __str__(self):
        return(f"{self.A}x + {self.B}y+ {self.C} = 0")
    
    def is_parallel(self,other_line):
        return (self.A*other_line.B == other_line.A*self.B)

    def distance(self,other_line):

        if not self.is_parallel(other_line):
            return "Lines are not parallel."

        numerator = abs(self.C - other_line.C)
        denominator = (self.A**2 + self.B**2)**0.5
        return (numerator/denominator)
    
    def point_on_line(self,point):
        result = self.A*point.x + self.B*point.y + self.C == 0
        if abs(result) < 1e-9:
            return "Point lie on the line"
        else:
            return "Point doesn't lie on the line"
        
point1 = CreatePoint(0,0)
point2 = CreatePoint(1,2)

line1 = CreateLine(1,0,2)
line2 = CreateLine(5,0,8)

# print(line1.point_on_line(point2))

# print(f"Parallel : {line1.is_parallel(line2)}")

print(line1.distance(line2))