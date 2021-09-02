# Algorithm Workbench kap 5
# Oppgave 4

# What will the following program display?

# def main():
#   x = 1
#   y = 3.4
#   print(x, y)
#   change_us(x, y)
#   print(x, y)
# 
# def change_us(a, b):
#   a = 0
#   b = 0
#   print(a, b)
# main()
# 
# 1. The program will first display the values x and y
#    which prints the numbers 1 and 3.4 respecitevly
# 2. The change_us function is then called with the arguments x and y
#    This function takes the arguments x and y and changes them both to 0
#    The function then prints the parameters a and b, which gives the value 0 and 0
# 3. The progam goes back to the main function and prints x and y
#    None of these values have been changed, so it will display 1 and 3.4 again.
# 
# The output of the code is:
# 1 3.4
# 0 0
# 1 3.4 

def main():
  x = 1
  y = 3.4
  print(x, y)
  change_us(x, y)
  print(x, y)

def change_us(a, b):
  a = 0
  b = 0
  print(a, b)
main()