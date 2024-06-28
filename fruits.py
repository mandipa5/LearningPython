fruits = []
total_fruits=int(input("Enter total number of fruits: "))
for i in range(1,total_fruits+1):
  fruit=input("Enter fruits: ")
  fruits.append(fruit)
print("\n-------\n")
print("All fruits entered are:")
for fruit in fruits:
  print(fruit)
