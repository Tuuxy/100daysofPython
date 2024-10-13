import tkinter


def button_clicked():
    my_label["text"] = user_input.get()

def button_clear():
    my_label["text"] = ""

window = tkinter.Tk()
window.title("Tuuxy's GUI Program")
window.minsize(width=500,height=500)
window.config(padx=20, pady=20)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="Change this by clicking the button after you entered text below!")
my_label.grid(column=0,row=0)

button = tkinter.Button(text="Click Me!", command=button_clicked)
button.grid(column=1,row=1)

user_input = tkinter.Entry(width=10)
print(user_input.get())
user_input.grid(column=3,row=2)

new_button = tkinter.Button(text="Clear Text", command=button_clear)
new_button.grid(column=2,row=0)


window.mainloop()
