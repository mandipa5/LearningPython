##print("Multiplication table of 9")
##for i in range(1,11):
  ##print(9*i)
  ##print(f"9 * {i} = {9*i}")



start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
for i in range(start,end+1):
  for j in range(1,11):
    print(f"{i} * {j} = {i*j}")
  print("\n----\n")
