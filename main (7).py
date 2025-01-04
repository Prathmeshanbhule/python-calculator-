x = float(input("Enter a number:"))
y = float(input("Enter a number:"))
print("1. Add")
print("2. subtract")
print('3. multiply')
print("4. divide")

choice = int(input("Enter your choice:"))

def divide(x,y):
  if y == 0:
    print("Error! Division by zero is not possible.")
  else:
    print(x/y)

if choice == 1:
  print(x+y)

if choice == 2:
  print(x-y)

if choice == 3:
  print(x*y)

if choice == 4:
  print(divide(x,y))