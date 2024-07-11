class Teacher:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
  def display(self):
    print(f"Name is {self.name}")
    print(f"Salary is {self.salary}")

t1 = Teacher(name="Ram Thapa", salary=15000)
t1.display()
t2 = Teacher(name="Maya Shrestha", salary=18000)
t2.display()
t3 = Teacher(name="Tara Gurung", salary=20000)
t3.display()
    