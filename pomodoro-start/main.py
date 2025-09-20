import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer1 = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer1)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)
    elif reps %2 ==0:
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    count_sec_left=0
    count_min_left=0
    canvas.itemconfig(timer_text, text=f"{count_min_left if count_min<10 else ''}{count_min}:{count_sec_left if count_sec<10 else ''}{count_sec}")
    if count>0:
        global timer1
        timer1 = window.after(1000, count_down, count-1 )
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔️"
        check_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer = Label(text="Timer", fg=GREEN,  bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 30, "bold"))
timer.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark=Label(text="✔️", fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)



window.mainloop()


