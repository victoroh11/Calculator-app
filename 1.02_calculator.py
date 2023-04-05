from tkinter import *
import math

root = Tk()
root.title("Calculator")

num1 = Entry(root)
num1.pack()

num2 = Entry(root)
num2.pack()

result = StringVar()

label = Label(root, textvariable=result)
label.pack()

rounding_scale = Scale(root, from_=0, to=10, orient=HORIZONTAL, label="Round up to:")
rounding_scale.pack()

def add():
    result.set(float(num1.get()) + float(num2.get()))

def subtract():
    result.set(float(num1.get()) - float(num2.get()))

def multiply():
    result.set(float(num1.get()) * float(num2.get()))

def divide():
    result.set(float(num1.get()) / float(num2.get()))

def square_root():
    result.set(round(math.sqrt(float(num1.get())), rounding_scale.get()))

def square():
    result.set(float(num1.get()) * float(num1.get()))

add_button = Button(root, text="+", command=add)
add_button.pack()

subtract_button = Button(root, text="-", command=subtract)
subtract_button.pack()

multiply_button = Button(root, text="*", command=multiply)
multiply_button.pack()

divide_button = Button(root, text="/", command=divide)
divide_button.pack()

square_root_button = Button(root, text="sqrt", command=square_root)
square_root_button.pack()

square_button = Button(root, text="sqr", command=square)
square_button.pack()
""" square features added """

root.mainloop()
