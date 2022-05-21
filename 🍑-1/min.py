import sys
def FindMin(lst):
  Min = int(lst[0])
  for itm in lst:
    if itm < Min:
      Min = itm
  return Min

if __name__ == "__main__":
  print(FindMin([int(sys.argv[i]) for i in range(1 , len(sys.argv))]))