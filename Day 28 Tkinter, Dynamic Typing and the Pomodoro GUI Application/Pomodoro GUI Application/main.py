import tkinter
import math
import time
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
timer =  None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timerText, text="00:00")
    timerLabel.config(text="Timer", fg=GREEN)
    checkmarkLabel.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 1:
        count_down(work_sec)
        timerLabel.config(text="Work", fg=GREEN)
    elif reps == 8:
        count_down(long_break_sec)
        timerLabel.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timerLabel.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    canvas.itemconfig(timerText, text=f"{count_min}:{count_sec:02}")
    if reps > 8:
        time.sleep(10)
        reset_timer()
    elif count == 0 and reps == 8:
        timer = window.after(1000, count_down, count-1)
    elif count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            mark = "✔"
            newText = ""
            for i in range(math.floor(reps/2)):
                newText += mark
            checkmarkLabel.config(text=newText)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#Tomato Image
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
timerText = canvas.create_text(100 , 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Timer Label
timerLabel = tkinter.Label(text="Timer",bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timerLabel.grid(column=1, row=0)

#Start Button
startButton = tkinter.Button(text="Start", font=(FONT_NAME, 10), highlightthickness=0, command=start_timer)
startButton.grid(column=0, row=2)

#Reset Button
resetButton = tkinter.Button(text="Reset", font=(FONT_NAME, 10), highlightthickness=0, command=reset_timer)
resetButton.grid(column=2, row=2)

#Checkmark Label
checkmarkLabel = tkinter.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10))
checkmarkLabel.grid(column=1, row=3)




window.mainloop()