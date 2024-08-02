import tkinter as tk
from tkinter import messagebox

def get_square():
  #Get value from textbox
  x = float(entry1.get())
  result = x * x
  messagebox.showinfo("Result",f"The square is {result}")

root = tk.Tk()
root.title("TC SquareCalculator")
root.geometry("300x200")

#For  Number
label1 = tk.Label(root,text="Enter the number: ")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

button = tk.Button(root,text="Find Square",command=get_square)
button.pack(pady=10)


#Run
root.mainloop()