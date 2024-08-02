from student import Student

total_sts = int(input("Enter the number of data that you want to enter for students: "))

for i in range(total_sts):
  n = input(f"Enter student {i+1} name: ")
  p = input(f"Enter student {i+1} number: ")
  s = Student(name = n, phone = p)
  f = open("contact.csv","a")
  f.write(f"{s.name},{s.phone}\n")
  f.close()
