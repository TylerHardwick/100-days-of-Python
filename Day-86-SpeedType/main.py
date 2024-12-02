import tkinter
from tkinter import *
from calc import Word_Counter
import math

FONT_NAME = "Courier"
GOLD = "#ffd700"
WHITE = "#FFFFFF"
GREEN = "#8BAB7C"
LIGHT_GREEN = "#B4DCA1"
DARK_GREEN = "#6A825E"
RED = "#FF0000"
timer = None
check_timer = None
countdown_min = 1
spell_label_list = []
turn = 0
started = False




wc = Word_Counter()

# --------- Timer --------------#


def reset_timer():
    text_entry.delete(0, 'end')
    wc.current_words = []
    wc.correct_words = 0
    wc.word_end = 5
    window.after_cancel(timer)
    timer_text.config(text="00:00")
    text_entry.delete(0, 'end')
    global turn
    turn = 0
    for num in range(5):
        spell_label_list[num].config(text="")
    global started
    started = False
    wc.reset_book()

def count_down(count):
   count_minute = math.floor(count / 60)
   count_second = count % 60
   if count_second <= 9:
       count_second = "0" + str(count_second)
   timer_text.config(text=f"{count_minute}:{count_second}")

   if count > 0:
       global timer
       timer = window.after(1000, count_down, count - 1)

   elif count == 0:
       score = wc.correct_words
       reset_timer()
       spell_label_list[2].config(text=f"Good job! Your WPM is {score}!", fg=GOLD)


def start_timer():
    global started
    if not started:
        started = True
        countdown_sec = countdown_min * 60
        count_down(countdown_sec)
        refresh_words()
        check()




# ----------- Dictionary/ words ------------#

def check():


    global check_timer
    check_timer = window.after(200, check)
    global turn
    current_input = str(user_input.get())
    input_words = current_input.split()
    if started:

        for word in input_words:

            if turn < 5:

                if word == wc.current_words[0] and word == input_words[-1]:
                    spell_label_list[turn].config(fg=RED)
                    wc.current_words.pop(wc.current_words.index(word))
                    wc.correct_words += 1
                    turn += 1

            else:
                current_input = None
                input_words = []

                refresh_words()





def refresh_words():
    global turn
    turn = 0
    wc.current_words = []
    wc.import_words()
    wc.current_words = wc.dictionary[wc.word_end - 5:wc.word_end]
    wc.word_end += 5
    text_entry.delete(0, 'end')

    for idx, label in enumerate(spell_label_list):
        label.config(text=f"{wc.current_words[idx]}", fg=DARK_GREEN)


# -------------UI Setup ------------#

window = Tk()
window.title("Tyler's SpeedTyper")
window.config(padx=100, pady=50, bg=LIGHT_GREEN)
title = Label(text="Tyler's SpeedTyper", font=(FONT_NAME, 35, "bold"), fg=DARK_GREEN, bg=LIGHT_GREEN)
title.grid(pady=(0,50),column=1, row=0)


#-------Frame---------#

frame = tkinter.Frame(window, bg=LIGHT_GREEN)
frame.grid(column=1, row=1)

# ------------------Phrase Labels ---------------- #
for num in range(5):
    spell_label_1 = Label(frame, text=f"", font=(FONT_NAME, 40, "bold"), fg=DARK_GREEN, bg=LIGHT_GREEN)
    spell_label_1.grid(padx=(0,50),pady=(0,50),column=num, row=0)
    spell_label_list.append(spell_label_1)


# -------------------------------------------------#

user_input = StringVar()
text_entry = Entry(width=40, font=(FONT_NAME, 30),textvariable=user_input)
text_entry.grid(pady=(0,50),column=1, row=2)
text_entry.focus()

timer_text =Label(text="00:00", font=(FONT_NAME, 35, "bold"), fg=WHITE, bg=LIGHT_GREEN)
timer_text.grid(column=1, row=3)

# --------- UI Buttons ------------ #
start_button = Button(text="Start", font=(FONT_NAME, 20, "bold"), fg=DARK_GREEN, bg=GREEN, width=18, command=start_timer)
start_button.grid(column=0, row=3)
restart_button = Button(text="Restart", font=(FONT_NAME, 20, "bold"), fg=DARK_GREEN, bg=GREEN, width=18, command=reset_timer)
restart_button.grid(column=2, row=3)



window.mainloop()



