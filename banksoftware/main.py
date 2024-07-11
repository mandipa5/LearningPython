from bank import Bank

option_text = """
What do you want to do[1-2]?
1. Add Customers
2. View details of Customers
"""

option = int(input(option_text))
if option == 1:
    b = Bank(id=0,name= "", phone=0, balance=0)
    b.id = int(input(f"Enter customer's id: "))
    b.name = input(f"Enter customer's name: ")
    b.phone = int(input(f"Enter customer's phone number: "))
    b.balance = float(input(f"Enter the balance: "))
    f = open('customers.csv','a')
    f.write(f"{b.id},{b.name},{b.phone},{b.balance}\n")
    f.close()
    print("Details Added Scuccessfully")
elif option == 2:
    f = open("customers.csv",'r')
    print("All Details are: \n------------------")
    print(f.read())
    print("------------------")
    