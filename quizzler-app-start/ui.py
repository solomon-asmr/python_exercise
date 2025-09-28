from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.score=0
        self.quiz = quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label=Label(text=f"Score: {self.score} ", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="questions",fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_btn_img = PhotoImage(file="images/true.png")
        self.right_btn = Button(image=right_btn_img, bg=THEME_COLOR, highlightthickness=0, command=self.check_true_answer)
        self.right_btn.grid(row=2, column=0)

        wrong_btn_img = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=wrong_btn_img, bg=THEME_COLOR, highlightthickness=0, command=self.check_true_answer)
        self.wrong_btn.grid(row=2, column=1)
        self.get_next_question()
        # self.check_false_answer()
        # self.check_true_answer()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the question! your final score is {self.quiz.score}/{self.quiz.question_number}")
            self.right_btn.config(state = "disabled")
            self.wrong_btn.config(state="disabled")

    def check_true_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def check_false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
