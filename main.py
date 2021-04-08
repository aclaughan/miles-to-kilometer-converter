from tkinter import *


def m2k():
    miles = float(entry.get())
    label_3.config(text=f"{miles * 1.609:0.2f}")


# Creating a new window and configurations
window = Tk()
window.title("miles to kilometer converter")
window.minsize(width=250
               , height=100)
window.config(padx=30, pady=30)

# Entry
entry = Entry(width=6)
entry.grid(row=0, column=1)

# Labels
label_1 = Label(text="Miles")
label_1.grid(row=0, column=2)

label_2 = Label(text="is equal to")
label_2.grid(row=1, column=0)

label_3 = Label(text="0")
label_3.grid(row=1, column=1)

label_4 = Label(text="km's")
label_4.grid(row=1, column=2)

# Button
button = Button(text="Calculate", command=m2k)
button.grid(row=2, column=1)

window.mainloop()
