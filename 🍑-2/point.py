class Point2D:
  def __init__(self ,x , y):
    self.x = x
    self.y = y
  def __add__(self , p2d):
    return Point2D(self.x + p2d.x , self.y + p2d.y)
  def __sub__(self , p2d):
    return Point2D(self.x - p2d.x , self.y - p2d.y)
  def Translate(self , x , y):
      return self + Point2D(x , y)
  def Reflect(self):
    return Point2D(-self.x , -self.y)
    
class Point3D(Point2D):
  def __init__(self , x , y , z):
    Point2D.__init__(self , x , y)
    self.z = z
  def __add__(self , p3d):
    p2d = Point2D(self.x , self.y) + Point2D(p3d.x , p3d.y) 
    return Point3D(p2d.x , p2d.y , self.z + p3d.z)
  def __sub__(self , p3d):
    p2d = Point2D(self.x , self.y) - Point2D(p3d.x , p3d.y)
    return Point3D(p2d.x , p2d.y , self.z - p3d.z)
  def Translate(self , x , y , z):
    return self + Point3D(x , y , z)
  def ReflectXY(self):
    point = Point2D(self.x , self.y).Reflect()
    return Point3D(point.x , point.y , self.z)
  def ReflectXZ(self):
    point = Point2D(self.x , self.z).Reflect()
    return Point3D(point.x , self.y , point.y)
  def ReflectYZ(self):
    point = Point2D(self.y , self.z).Reflect()
    return Point3D(self.x , point.x , point.y)

p3d1 = Point3D(10 , 20 , 30)
p3d2 = Point3D(20 , 40 , 50)
p3d3 =  p3d2 + p3d1 - p3d2

p3d4 = p3d3.ReflectXY() 

print(p3d3.x , p3d3.y , p3d3.z)
print(p3d4.x , p3d4.y , p3d4.z)