import tkinter as tk

FONT = ("Arial", 14, "bold")


def miles_km_converter():
    miles = miles_input.get()
    km["text"] = int(miles) * 1.6093


window = tk.Tk()
window.title("Miles to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=40, pady=20)

text_miles = tk.Label(text="miles", font=FONT)
text = tk.Label(text="is equal to ", font=FONT)
text_km = tk.Label(text="km", font=FONT)
miles_input = tk.Entry(width=10)
km = tk.Label(text="0", font=FONT)

text_miles.grid(column=1, row=0)
text.grid(column=2, row=0)
text_km.grid(column=4, row=0)
miles_input.grid(column=0, row=0)
km.grid(column=3, row=0)


button = tk.Button(text="Calculate", command=miles_km_converter)
button.grid(column=2, row=1)


window.mainloop()