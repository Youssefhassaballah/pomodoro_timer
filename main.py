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
check_mark = "✔️"
done = ""
timer = None
reps = 0
use = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def start_timer():
    global timer
    if use != 0:
        window.after_cancel(timer)
    global done, check, reps, check_mark
    reps += 1
    if reps % 2 != 0:
        title_lapel.config(text="Work")
        count_down(WORK_MIN*60)
    elif reps % 8 != 0:
        title_lapel.config(text="Short break")
        count_down(SHORT_BREAK_MIN * 60)
    else:
        title_lapel.config(text="Long break")
        count_down(LONG_BREAK_MIN * 60)


def count_down(count):
    global use
    use += 1
    global timer, check_mark, done
    minutes = int(count / 60)
    seconds = count % 60
    seconds = int(seconds)
    if minutes < 10:
        minutes_text = f"0{minutes}"
    else:
        minutes_text = f"{minutes}"

    if seconds < 10:
        seconds_text = f"0{seconds}"
    else:
        seconds_text = f"{seconds}"

    canvas.itemconfig(text_timer, text=minutes_text+":"+seconds_text)
    if count >= 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        sessions = int(reps/2)
        done = ""
        for i in range(sessions):
            done += check_mark
        check.config(text=done)


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global timer, reps, done, use
    window.after_cancel(timer)
    use = 0
    canvas.itemconfig(text_timer, text="00:00")
    reps = 0
    title_lapel.config(text="Timer")
    done = ""
    check.config(text=done)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)
tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)
canvas.create_image(100, 112, image=tomato_image)

text_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))


title_lapel = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN)
title_lapel.config(bg=YELLOW)
title_lapel.grid(column=1, row=0)

start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

reset_b = Button(text="Reset", command=reset)
reset_b.grid(column=2, row=2)

check = Label(font=(FONT_NAME, 10, "bold"), fg=GREEN)
check.grid(column=1, row=3)
check.config(bg=YELLOW)

window.mainloop()
