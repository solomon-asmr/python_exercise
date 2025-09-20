from tkinter import *

window = Tk()
window.minsize(width=500, height=250)
window.title("Mile to Km Converter")
window.config(padx=100, pady=90)

input_mile = Entry()
input_mile.grid(row=0, column=1)


mile = Label(text="Miles")
mile.grid(row=0, column=2)


is_equal= Label(text="is equal to")
is_equal.grid(row=1, column=0)


km_label=Label(text="0")
km_label.grid(row=1, column=1)

km_la=Label(text="KM")
km_la.grid(row=1, column=2)

def miles_to_km():
    mil= int(input_mile.get())
    result=mil * 1.60934
    km_label.config(text=result)


button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)









window.mainloop()