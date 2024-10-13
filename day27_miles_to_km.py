import tkinter


def miles_to_km():
    miles = entry.get()
    if not entry.get():
        miles = 0
    km = float(miles) * 1.60934
    label_converted["text"] = str(round(km,2))


window = tkinter.Tk()
window.config(padx=10,pady=10)
window.minsize(width=300, height=200)
window.title("Mile to Km converter")

entry = tkinter.Entry(width=5)
entry.insert(1,string="0")
entry.grid(row=0,column=1)

label_equal = tkinter.Label(text="is equal to")
label_equal.grid(row=1,column=0)

label_miles = tkinter.Label(text="Miles")
label_miles.grid(row=0,column=2)

label_km = tkinter.Label(text="Km")
label_km.grid(row=1,column=2)

label_converted = tkinter.Label(text="0")
label_converted.grid(row=1,column=1)

button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(row=2,column=1)


window.mainloop()