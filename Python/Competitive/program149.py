import tkinter as tk

root = tk.Tk()

root.title("Area of circle")
root.geometry("400x300")

tk.Label(root,text="Enter radius(cm)").pack()
radius = tk.Entry(root)
radius.pack()

labelresult=tk.Label(root,text="")
labelresult.pack()

def Area():
    no = int(radius.get())

    area = 3.14 * no * no

    labelresult.config(text= f"Area is {area} cm2")

tk.Button(root,text="find",command=Area).pack()

tk.mainloop()

