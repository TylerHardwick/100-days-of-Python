from tkinter import *
from converter import Converter

class Gui_display():

    def __init__(self):
        self.FONT_NAME = "Calibri"
        self.WHITE = "#FFFFFF"
        self.DARK_BLUE = "#342FB6"
        self.LIGHT_BLUE = "#D4F9FA"
        self.BLUE = "#8AE2E3"
        self.convert = Converter()

# ---------------UI Setup ------------#
    def show_ui(self):
        window = Tk()
        window.title("Tyler's Watermark Tool")
        window.config(padx=100, pady=50, bg=self.LIGHT_BLUE)

        timer_label = Label(text="Tyler's Watermarker", font=(self.FONT_NAME, 35, "bold"), fg=self.DARK_BLUE, bg=self.LIGHT_BLUE)
        timer_label.grid(pady=(0,200),column=2, row=0)



# ------------ UI Buttons ------------ #

        select_button = Button(text="Select File", font=(self.FONT_NAME, 20, "bold"), fg=self.DARK_BLUE, bg=self.BLUE, width=18, command=self.convert.open_file)
        select_button.grid(column=1, row=1)
        all_button = Button(text="Watermark All", font=(self.FONT_NAME, 20, "bold"), fg=self.DARK_BLUE, bg=self.BLUE, width=18, command=self.convert.convert_all)
        all_button.grid(column=2, row=1)
        change_watermark = Button(text="Change Watermark", font=(self.FONT_NAME, 20, "bold"), fg=self.DARK_BLUE, bg=self.BLUE, width=18, command=self.convert.open_watermark_file)
        change_watermark.grid(column=3, row=1)


        window.mainloop()




