import tkinter as tk
from tkinter import messagebox

def get_simpleinterest():
  #Get value
  principal = float(entry1.get())
  time = float(entry2.get())
  rate = float(entry3.get())

  interest = (principal*time*rate)/100
  messagebox.showinfo("Result",f"The Simple Interest is {interest}")

root = tk.Tk()
root.title("Simple Interest Finder")
root.geometry("500x300")

#For Principal
label1 = tk.Label(root,text="Enter principal amount: ")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

#For Time
label2 = tk.Label(root,text="Enter time(in years): ")
label2.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

#For Rate
label3 = tk.Label(root,text="Enter rate: ")
label3.pack(pady=5)
entry3 = tk.Entry(root)
entry3.pack(pady=5)

button = tk.Button(root,text="Find Simple Interest",command=get_simpleinterest)
button.pack(pady=10)



#Run
root.mainloop()