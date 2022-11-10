from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("tjh's Quiz")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="", fill=THEME_COLOR, width=280,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        self.score_counter = Label()
        self.score_counter.config(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 16))
        self.score_counter.grid(row=0, column=1)

        tick_img = PhotoImage(file="./images/true.png")
        self.tick_button = Button(image=tick_img, highlightthickness=0, command=self.check_answer_true)
        self.tick_button.grid(row=2, column=0)

        cross_img = PhotoImage(file="./images/false.png")
        self.cross_button = Button(image=cross_img, highlightthickness=0, command=self.check_answer_false)
        self.cross_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_counter.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Quiz Complete \n Final score: {self.quiz.score}/10")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def check_answer_true(self):
        result = self.quiz.check_answer("True")
        self.give_feedback(result)

    def check_answer_false(self):
        result = self.quiz.check_answer("False")
        self.give_feedback(result)

    def give_feedback(self, result):
        if result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


