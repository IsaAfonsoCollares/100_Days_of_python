import tkinter as tk
FONT = ("Arial", 24, "bold")
window = tk.Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
my_label = tk.Label(text="Converter", font=FONT)
my_label.pack()
my_label["text"] = "New York"




new = tk.Entry(width=10)
new.pack()

def button_click():
    new_text = new.get()
    my_label.config(text=new_text)


button = tk.Button(text="Click me", command=button_click)
button.pack()


window.mainloop()