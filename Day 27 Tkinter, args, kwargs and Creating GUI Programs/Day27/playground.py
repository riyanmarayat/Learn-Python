#Part 207 *args: Many Positional Arguments
# def add(*nums): #args is a tuple
#     sum = 0
#     for num in nums:
#         sum += num
#     return sum
#
# print(add(1, 2, 3, 4, 5))  # 15

#Part 208 **kwargs: Many Keyword Arguments
# def calculate(n, **kwargs): #kwargs is a dictionary
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
#
# calculate(2, add=3, multiply=5) #25
#
# class Car:
#
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#
# my_car = Car(make="Nissan")
# print(my_car.model) #None


#Part 209 Buttons, Entry, and Setting Component Options
# import tkinter #tkinter is a module
#
# window = tkinter.Tk() #Tk is a class
# window.title("My First GUI Program") #title is a method
# window.minsize(width=500, height=300) #minsize is a method
#
# #Label
#
# my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold")) #Label is a class
# my_label.pack() #pack is a method
#
# my_label["text"] = "New Text"  #same as my_label.config(text="New Text")
# my_label.config(text="New Text") #same as my_label["text"] = "New Text"
#
# #Button
#
# def button_clicked():   #button_clicked is a function
#     print("I got clicked") #print is a function
#     new_text = input.get() #get is a method
#     my_label.config(text=new_text) #config is a method
#
#
# button = tkinter.Button(text="Click Me", command=button_clicked) #Button is a class
# button.pack() #pack is a method
#
# #Entry
#
# input = tkinter.Entry(width=10) #Entry is a class
# input.pack() #pack is a method
# print(input.get()) #get is a method
#
#
#
# window.mainloop() #mainloop is a method


#Part 211 Tkinter Layout Managers:pack(), place(), grid()
from tkinter import *

def button_clicked():   #button_clicked is a function
    print("I got clicked") #print is a function
    new_text = input.get() #get is a method
    my_label.config(text=new_text) #config is a method

window = Tk() #Tk is a class
window.title("My First GUI Program") #title is a method
window.minsize(width=500, height=300) #minsize is a method
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold")) #Label is a class
my_label.config(text="New Text") #same as my_label["text"] = "New Text"
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click Me", command=button_clicked) #Button is a class
button.grid(column=1, row=1)

newButton = Button(text="Click Me 2", command="Button had been clicked")
newButton.grid(column=2, row=0)

#Entry
input = Entry(width=10) #Entry is a class
print(input.get()) #get is a method
input.grid(column=3, row=2)


window.mainloop()