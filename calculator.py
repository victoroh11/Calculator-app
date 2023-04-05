from tkinter import *

root = Tk()
root.title("Calculator")

num1 = Entry(root)
num1.pack()

num2 = Entry(root)
num2.pack()

result = StringVar()

label = Label(root, textvariable=result)
label.pack()

def add():
    result.set(float(num1.get()) + float(num2.get()))

def subtract():
    result.set(float(num1.get()) - float(num2.get()))

def multiply():
    result.set(float(num1.get()) * float(num2.get()))

def divide():
    result.set(float(num1.get()) / float(num2.get()))

add_button = Button(root, text="+", command=add)
add_button.pack()

subtract_button = Button(root, text="-", command=subtract)
subtract_button.pack()

multiply_button = Button(root, text="*", command=multiply)
multiply_button.pack()

divide_button = Button(root, text="/", command=divide)
divide_button.pack()

root.mainloop()