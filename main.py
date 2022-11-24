from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="Miles to KMs Converter", font=("Arial", 24, "bold"))
my_label.grid(row=0,column=1)

# Label 2
my_label_2 = Label(text="0", font=("Arial", 24, "bold"))
my_label_2.grid(row=3,column=1)

# Label 3
my_label_3 = Label(text="is equal to", font=("Arial", 24, "bold"))
my_label_3.grid(row=3,column=0)

# Label 4
my_label_4 = Label(text="KMs", font=("Arial", 24, "bold"))
my_label_4.grid(row=3,column=2)

# Button
def button_clicked():
    new_text = int(input.get())
    new_text = new_text*1.6
    my_label_2.config(text=new_text)

button = Button(text="Calculate", command=button_clicked)
button.grid(row=4,column=1)

# Entry
input = Entry(width=10)
input.grid(row=2,column=1)

window.mainloop()