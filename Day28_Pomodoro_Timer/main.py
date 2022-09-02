from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = 1*60
SHORT_BREAK_SEC = 1*60
LONG_BREAK_SEC = 1*60
reps = 0
checks_text = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_count():
    print("Hi")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global reps
    reps += 1
    if reps % 8 == 0:
        timer_label["text"] = "LONG BREAK"
        countdown(LONG_BREAK_SEC)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_SEC)
        timer_label["text"] = "BREAK"
    else:
        countdown(WORK_SEC)
        timer_label["text"] = "WORK"

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global checks_text
    count_minutes = floor(count/60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        window.after(1000, countdown, count-1)
    else:
        if reps % 2 == 0:
            checks_text += "✓"
        check_marks_label["text"] = checks_text
        start_count()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg=GREEN)

timer_label = Label(text="Timer", bg=GREEN, fg=RED, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=2, row=1)

canvas = Canvas(width=200, heigh=224, bg=GREEN, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)


start_button = Button(text="Start", width=10, command=start_count, highlightthickness=0,
                      font=(FONT_NAME, 14, "bold"))
start_button.grid(column=1, row=3)
check_marks_label = Label(fg=RED, bg=GREEN, font=(FONT_NAME, 14, "bold"))
check_marks_label.grid(column=2, row=4)
reset_button = Button(text="Reset", width=10, command=reset_count, highlightthickness=0,
                      font=(FONT_NAME, 14, "bold"))
reset_button.grid(column=3, row=3)

window.mainloop()
