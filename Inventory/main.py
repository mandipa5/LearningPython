from products import Products

for i in range(1,11):
   d = input(f"Enter the ID for product {i}: ")
   n = input(f"Enter the name for product {i}: ")
   q = input(f"Enter the quantity for product {i}:")
   p = input(f"Enter the price for product {i}:")
   Prod = Products(id = d, name = n, qty = q, price = p)
   f = open("List.csv","a")
   f.write(f"{Prod.id},{Prod.name},{Prod.qty},{Prod.price}\n")
   f.close()
   
   
