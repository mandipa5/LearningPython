import tkinter as tk
from tkinter import messagebox

def get_roi():
  #Get value from textbox
  investment = float(entry1.get())
  income = float(entry2.get())

  result = investment + income
  messagebox.showinfo("Result",f"The Return of Investment is {result}")

root = tk.Tk()
root.title("ROI Finder")
root.geometry("300x200")

#For Investment
label1 = tk.Label(root,text="Enter investment: ")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

#For Income
label2 = tk.Label(root,text="Enter income: ")
label2.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

button = tk.Button(root,text="Find ROI",command=get_roi)
button.pack(pady=10)

#Run
root.mainloop()