#area of a triangle given a,b , c
#on Heron's formula (root(s(s-a) (s-b) (s-c)))
import math
def AreaOfTriangle(a,b,c):
  if(a + b >= c) and (a + c >= b) and (b + c >= a):
    s =  (a + b + c)/2
    return (s * (s - a) * (s - b) * (s - c)) * math.sqrt(2)

if __name__ == "__main__":
    print("Enter 3 sides of triangle:")
    print("AREA =" , AreaOfTriangle(
                                     int(input("SIDE1 = ")),
                                     int(input("SIDE2 = ")),
                                     int(input("SIDE3 = "))
                                   )
        )
