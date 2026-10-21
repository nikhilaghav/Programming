import tkinter as tk

root = tk.Tk()

root.title("find Largest Number")
root.geometry("400x300")

tk.Label(root,text = "Enter first number").pack()
entry1 =tk.Entry(root)
entry1.pack()

tk.Label(root,text = "Enter second number").pack()
entry2 =tk.Entry(root)
entry2.pack()

tk.Label(root,text = "Enter third number").pack()
entry3 =tk.Entry(root)
entry3.pack()

labelresult = tk.Label(root,text="")
labelresult.pack()

def Largest():
    no1 = int(entry1.get())
    no2 = int(entry2.get())
    no3 = int(entry3.get())

    if no1 > no2 and no1 > no3:
            labelresult.config(text="largest number is:"+str(no1))

    elif no2> no1 and no2 > no3:
            labelresult.config(text="largest number is:"+str(no2))

    else:
            labelresult.config(text="largest number is:"+str(no3))
            
tk.Button(root,text="find",command=Largest).pack()

root.mainloop()