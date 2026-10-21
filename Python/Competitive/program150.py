import tkinter as tk

root = tk.Tk()

root.title("voter eligibility checker")
root.geometry("400x300")

tk.Label(root,text="Enter your name").pack()
name = tk.Entry(root)
name.pack()

tk.Label(root,text="Enter your age").pack()
age = tk.Entry(root)
age.pack()

labelresult = tk.Label(root,text="")
labelresult.pack()

def ChkEligibilty():
    no = int(age.get())

    if no >=18:
        labelresult.config(text="You are eligible to vote")
    else:
        labelresult.config(text="You are not eligible ")

tk.Button(root,text="check eligibilty", command=ChkEligibilty).pack()

tk.mainloop()
