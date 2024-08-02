try:
  num1 = input("Enter number1: ")
  num2 = input("Enter number2: ")
  sum = float(num1) + float(num2)
  print(f"The total sum is: {sum}")
except:
  print("Please enter all numeric values")
finally:
  print("Back to program")