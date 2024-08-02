class Products:
  def __init__(self, id, name, qty, price):
    self.name = name
    self.id = id
    self.qty = qty
    self.price = price
  def display(self):
    print(f"ID is: {self.id}, Name is: {self.name}, Quantity is: {self.qty}, Price is: {self.price}")
    