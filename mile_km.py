from tkinter import *

window = Tk()
window.title("mile to km",)
window.minsize(height=300,width=500)
window.config(padx=200,pady=200)

def mile_to_km():
    m= input.get()
    km_equilivant["text"] = str(float(m) * 1.60934)


#Entery
input = Entry(width=10)
input.grid(column=1,row=0)

#Label
mile = Label(text="Mile")
mile.grid(column=2,row=0)
is_equal = Label(text="is equal to")
is_equal.grid(column=0 ,row=1)
km = Label(text="Km")
km.grid(column=2 ,row=1)
km_equilivant = Label(text="")
km_equilivant.grid(column=1 ,row=1)
#Button
button = Button(text="calculate",command=mile_to_km)
button.grid(column=1 ,row=2)
window.mainloop()