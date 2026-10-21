import tkinter as tk

root = tk.Tk()

root.title("Login Form")
root.geometry("400x300")

correct_username = "nikhil"
correct_pwd = "12345"

tk.Label(root,text="Enter username").pack()
name = tk.Entry(root)
name.pack()

tk.Label(root,text="Enter password").pack()
pwd = tk.Entry(root)
pwd.pack()

labelresult = tk.Label(root,text="")
labelresult.pack()

def Validate():
    username = name.get()
    password = pwd.get()

    if username == correct_username and password == correct_pwd:
        labelresult.config(text="Login succesfull",fg="green")

    else:
        labelresult.config(text="Login failed",fg="red")

tk.Button(root,text="Login", command=Validate).pack()

tk.mainloop()
