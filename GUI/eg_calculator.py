import tkinter as tk
from tkinter import messagebox

def get_calculation():
  #Get value from textbox
  value1 = float(entry1.get())
  value2 = float(entry2.get())

  result_sum = value1 + value2
  result_difference = value1 - value2
  result_multiply = value1*value2
  result_divide = value1%value2
  messagebox.showinfo("Result",f"The sum is {result_sum}")
  messagebox.showinfo("Result",f"The difference is {result_difference}")
  messagebox.showinfo("Result",f"The multiplication is {result_multiply}")
  messagebox.showinfo("Result",f"The remainder is {result_divide}")


root = tk.Tk()
root.title("TC Calculator")
root.geometry("300x200")

#For First Number
label1 = tk.Label(root,text="Enter first number: ")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

#For Second Number
label2 = tk.Label(root,text="Enter second number: ")
label2.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

button = tk.Button(root,text="Find Sum,Difference,Multiplication and division",command=get_calculation)
button.pack(pady=10)




#Run
root.mainloop()