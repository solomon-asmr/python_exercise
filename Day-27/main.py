
from tkinter import *

window = Tk()
window.title("My First GUI program")
window.minsize(width=600, height=400)

# label
my_label = Label(text="I Am a label", font=("italic", 15, "bold"))
my_label.pack()

def got_clicked():
    new_text=input_text.get()
    my_label.config(text=new_text)
# my_label["text"]="New Text"


# buttons
my_button = Button(text="Click me!", command=got_clicked)
my_button.pack()

# Entry
input_text=Entry(width=10)
input_text.pack()
print(input_text.get())




window.mainloop()