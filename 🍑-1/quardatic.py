#quadratic equation 
#sridhar acharya's formula
#  (-b (+/-) ((b ** 2 - 4 * a * c) ** (0.5))) / 2a

def GetRoots(a , b , c):
    UnderRoot = (b ** 2) - 4 * a * c
    temp2a = 2 * a
    tempB = (-b) / temp2a
    temp = (abs(UnderRoot)) ** (0.5) / temp2a
    if UnderRoot < 0:
        temp = str(temp) + "i" 
        tempB = str(tempB) 
        return tempB + '+' + temp , tempB + '-' + temp
    else:
        return tempB + temp , tempB - temp

if __name__ == "__main__":
    			print("ENTER a , b , c of quardatic equation like ax^2 + bx + c = 0")
    			r1 ,r2 = GetRoots(
                        			int(input("a = ")),
                        			int(input("b = ")),
                        			int(input("c = "))
                     		    )
    			print("ROOTS ARE", r1 , r2)
