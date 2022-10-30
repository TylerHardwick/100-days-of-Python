from tkinter import *


def calc():
    user_miles = float(miles_input.get())
    if radio_used():
        new_km = user_miles * 0.621371

    elif not radio_used():
        new_km = user_miles * 1.60934
    km_output_label.config(text=round(new_km, 2))

 
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=30, pady=20)

calc_button = Button(text="Calculate", command=calc)
calc_button.grid(column=1, row=2)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)
miles_input.insert(END,string="0")

km_output_label = Label(text="0")
km_output_label.grid(column=1, row=1)

miles_text_label = Label(text="Miles")
miles_text_label.grid(column=2, row=0)

equal_text_label = Label(text="is equal to")
equal_text_label.grid(column=0, row=1)

km_text_label = Label(text="Km")
km_text_label.grid(column=2, row=1)



def radio_used():
    calc_select = radio_state.get()
    if calc_select > 0:
        km_text_label.config(text="Miles")
        miles_text_label.config(text="Km")
        return True
    else:
        km_text_label.config(text="Km")
        miles_text_label.config(text="Miles")
        return False


#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Miles to Km", value=0, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Km to Miles", value=1, variable=radio_state, command=radio_used)
radiobutton1.grid(column=3, row=0)
radiobutton2.grid(column=3, row=1)
radiobutton1.select()
radiobutton2.config(padx=30)








window.mainloop()

