import tkinter

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kmValue_label.config(text=f"{km}")

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

#Label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

isEqualTo_label = tkinter.Label(text="is equal to")
isEqualTo_label.grid(column=0, row=1)

kmValue_label = tkinter.Label(text="0")
kmValue_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

#Button
calculate_button = tkinter.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

#Entry
miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=0)

window.mainloop()