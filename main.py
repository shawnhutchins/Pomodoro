import tkinter as tk
from tkinter import PhotoImage
import math

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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    print(reps)
    work_sec = WORK_MIN# * 60
    short_break_sec = SHORT_BREAK_MIN# * 60
    long_break_sec = LONG_BREAK_MIN# * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
    elif reps % 2 != 0:
        count_down(work_sec)
    else:
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro?")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

#Timer label
timer_label = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=0, column=1)

#Label for checkmarks for each session completed, make green with fg=, find check from wiki
checkmarks = tk.Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
checkmarks.grid(row=3, column=1)

#start and restart buttons
start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

restart_button = tk.Button(text="Restart", highlightthickness=0)
restart_button.grid(row=2, column=2)

window.mainloop()