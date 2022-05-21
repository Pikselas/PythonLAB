try:
  #0 div error
  10 / 0
except ZeroDivisionError as e:
 print(e)

class UserDefinedError(Exception):
  pass

try:
  #file not found
  with open("op.pp") as op:
    pass
except FileNotFoundError as e:
  print(e)
  
try:
  raise UserDefinedError()
except Exception:
  print("User defined error")