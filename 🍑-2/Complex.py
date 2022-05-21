class Complex:
  def __init__(self , rel , img):
    self.real = rel
    self.img = img
  def __add__(self , cmp):
    return Complex(self.real + cmp.real , self.img + cmp.img)
  def __sub__(self , cmp):
     return Complex(self.real - cmp.real , self.img - cmp.img)
  def __mul__(self , cmp):
     rel_prt = self.real * cmp.real - self.img * cmp.img
     img_prt = (self.real * cmp.img) + (self.img * cmp.real)
     return Complex(rel_prt , img_prt)
  def __eq__(self , cmp):
     return self.real == cmp.real and self.img == cmp.img
  def __str__(self):
    sign = "+"
    if self.img < 0:
      sign = ""
    return str(self.real)  + sign + str(self.img) + "i"

Cmp1 = Complex(1 , 2)
Cmp2 = Complex(1 , 2)

Cmp3 = Cmp1 - Cmp2
Cmp4 = Cmp1 * Cmp2
print(str(Cmp3))
print(Cmp1 == Cmp2)