import tkinter as tk

root = tk.Tk()

root.title("Addition")
root.geometry("400x300")

tk.Label(root,text = "Enter first number").pack()
entry1 =tk.Entry(root)
entry1.pack()

tk.Label(root,text = "Enter second number").pack()
entry2 =tk.Entry(root)
entry2.pack()

labelresult = tk.Label(root,text="")
labelresult.pack()

def Addition():
    no1 = int(entry1.get())
    no2 = int(entry2.get())

    ans = no1+ no2

    labelresult.config(text="Addition is"+str(ans))

tk.Button(root,text="Addition",command=Addition).pack()

root.mainloop()