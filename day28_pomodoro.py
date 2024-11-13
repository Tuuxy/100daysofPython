import os
import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK = "✓"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0
paused = False
paused_time = 0
current_phase = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, reps, paused, paused_time, current_phase

    if timer is not None:
        window.after_cancel(timer)

    timer = None
    paused = False
    paused_time = 0
    current_phase = None
    start_button.config(text="Start")
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_pause_timer():
    global paused

    if timer is None and not paused:
        start_timer()
    elif paused:
        resume_timer()
    else:
        pause_timer()

def start_timer():
    global reps, timer, paused, paused_time, current_phase

    if timer is None and not paused:
        start_button.config(text="Pause")
        reps += 1
        
        if reps % 8 == 0:
            current_phase = "long_break"
            count_down(LONG_BREAK_MIN * 60)
            title_label.config(text="Break", fg=RED)
        elif reps % 2 == 0:
            current_phase = "short_break"
            count_down(SHORT_BREAK_MIN * 60)
            title_label.config(text="Break", fg=PINK)
        else:
            current_phase = "work"
            count_down(WORK_MIN * 60)
            title_label.config(text="Work", fg=GREEN)

def resume_timer():
    global paused, timer

    if paused and paused_time > 0:
        paused = False
        start_button.config(text="Pause")
        count_down(paused_time)

# ---------------------------- PAUSE FUNCTION ------------------------------- #
def pause_timer():
    global timer, paused

    if not paused:
        paused = True
        start_button.config(text="Resume")
        if timer is not None:
            window.after_cancel(timer)
            timer = None

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer, paused_time, current_phase
    
    if not paused:
        paused_time = count
        count_min = math.floor(count / 60)
        count_sec = count % 60
        
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        
        if count > 0:
            timer = window.after(1000, count_down, count - 1)
        else:
            timer = None
            start_button.config(text="Start")
            if not paused:
                marks = ""
                work_sessions = math.floor(reps/2)
                for _ in range(work_sessions):
                    marks += CHECK
                check_marks.config(text=marks)
                start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image_path = os.path.join(os.path.dirname(__file__), "tomato.png")
tomato_img = PhotoImage(file=image_path)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_pause_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 20, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()