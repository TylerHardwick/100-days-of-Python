from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")


try:
    word_df = pandas.read_csv("./data/words_to_learn.csv")
    to_learn = word_df.to_dict(orient="records")
except FileNotFoundError:
    word_df = pandas.read_csv("./data/french_words.csv")
    to_learn = word_df.to_dict(orient="records")

current_card = {}


def flip_card():
    canvas.itemconfig(canvas_card, image=card_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


def create_new_card():
    canvas.itemconfig(canvas_card, image=card_front)
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


def know_card():
    to_learn.remove(current_card)
    to_learn_df = pandas.DataFrame(to_learn)
    to_learn_df.to_csv("./data/words_to_learn.csv", index=False)
    create_new_card()


# =======UI===========

window = Tk()
window.title("Tyler's Flash Cards")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas_card = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
word_text = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
x_button = Button(image=wrong_img, highlightthickness=0, command=create_new_card)
x_button.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
tick_button = Button(image=right_img, highlightthickness=0, command=know_card)
tick_button.grid(row=1, column=1)

create_new_card()

window.mainloop()