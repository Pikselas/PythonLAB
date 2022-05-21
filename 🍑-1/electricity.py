def CalculateCost(unit):
   if unit <= 50:
       return unit * 5.0
   elif unit <= 100:
      return 250 + (unit - 50) * 6.5
   elif unit <= 200 :
       return 250 + 325 + 800 + (unit - 200) * 10

if __name__ == "__main__":
    print(CalculateCost(int(input("ENTER UNIT :"))))
