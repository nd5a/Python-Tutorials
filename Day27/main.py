# # from tkinter import *

# # window = Tk()
# # window.title("MY First GUI Program")
# # window.minsize(width=500, height=300)

# # # label

# # my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# # my_label.pack()

# # # import turtle

# # # turtle.Turtle()

# # # import turtle

# # # tim = turtle.Turtle()
# # # tim.write("Some Text", font=("Times New Roman", 40, "bold"))

# # my_label["text"] = "New Text"
# # my_label.config(text="New Text")

# # # button

# # def button_clicked():
# #     print("I Got clicked")
# #     # my_label.config(text="Button Got Clicked")
# #     my_label.config(text=input.get())
# # button = Button(text="Click me", command=button_clicked)
# # button.pack()

# # # Entry
# # input = Entry(width=19)
# # input.pack()

# # # print(input.get())

# # window.mainloop()


# from tkinter import *

# # Crating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)

# # labels
# label = Label(text="This is old Text")
# label.config(text="This is new Text")
# label.pack()

# # buttons
# def action():
#     print("Do Something")

# # Calls action() when presssed
# button = Button(text="Click Me", command=action)
# button.pack()

# # Entries
# entry = Entry(width=30)

# # Add some text to begin with
# entry.insert(END, string="Some Text to begin with.")

# # gets text in entry
# print(entry.get())
# entry.pack()

# # text
# text = Text(height=5, width=30)
# # puts cursor in textbox
# text.focus()
# # Adds some text to begin with
# text.insert(END, "Example of multi - line text entry")
# # Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()


# # Spin box
# def spinbox_used():
#     # gets the current value in spinbox
#     print(spinbox.get())

# spinbox = Spinbox(from_ = 0, to=10, width=5, command=spinbox_used)
# spinbox.pack()


# # Scale
# # Called with current scale value
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()

# # Check Button
# def checkbutton_used():
#     # prints 1 if on button checked, otherwise 0
#     print(checked_state.get())

# # Variables to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()

# # Radiobutton

# def radio_used():
#     print(radio_state.get())

# # Variables to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()

# # List Box
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))

# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]

# for item in fruits:
#     listbox.insert(fruits.index(item), item)

# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()

from tkinter import *

window = Tk()
window.title("MY First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack(side="left")
# my_label.place(x = 100, y = 200)
my_label.grid(column=0, row=0)

# button

def button_clicked():
    print("I Got clicked")
    # my_label.config(text="Button Got Clicked")
    my_label.config(text=input.get())
button = Button(text="Click me", command=button_clicked)
# button.pack(side="left")
button.grid(column=1, row=1)

new_button = Button(text="Click on New Button", command=button_clicked)
# button.pack(side="left")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
# input.pack(side="left")
input.grid(column=3, row=2)

# print(input.get())

window.mainloop()
