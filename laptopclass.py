class Laptop:
  def __init__(self, id, name, ram):
    self.id = id
    self.name = name
    self.ram = ram
  def display(self):
    print(f"ID is {self.id} \t Name is {self.name} \t RAM is {self.ram} ")
    
l1 = Laptop(id = 1, name="Dell", ram = "8GB")
l1.display()
l2 = Laptop(id = 2, name="MAC", ram = "16GB")
l2.display()
l3 = Laptop(id = 3, name="Predator", ram = "16GB")
l3.display()
    