import time
import tkinter as tk
from tkmacosx import Button

timer_popup = None


def format_time(seconds):
    whole, ms = int(seconds), seconds - int(seconds)
    mins, secs = divmod(whole, 60)
    hours, mins = divmod(mins, 60)

    if hours > 0:
        return f"{hours}h {mins}m {secs + ms:.2f}s"
    if mins > 0:
        return f"{mins}m {secs + ms:.2f}s"
    return f"{seconds:.2f} seconds"


def open_timer_popup():
    global timer_popup

    if timer_popup is not None and timer_popup.winfo_exists():
        timer_popup.lift()
        return

    start_time = None
    elapsed_time = 0.0
    is_running = False

    timer_popup = tk.Tk()
    timer_popup.title("NCTC Timer")
    timer_popup.geometry("390x120")
    timer_popup.attributes("-topmost", True)
    timer_popup.configure(bg="#1E1E1E")

    label = tk.Label(
        timer_popup,
        text="0.00 seconds",
        font=("Helvetica", 32, "bold"),
        fg="#00E5FF",
        bg="#1E1E1E",
    )
    label.pack(pady=(12, 8))

    def tick():
        if is_running and timer_popup.winfo_exists():
            current = elapsed_time + (time.time() - start_time)
            label.config(text=format_time(current))
            timer_popup.after(100, tick)

    def on_start():
        nonlocal is_running, start_time
        if not is_running:
            is_running = True
            start_time = time.time()
            tick()

    def on_stop():
        nonlocal is_running, elapsed_time
        if is_running:
            is_running = False
            elapsed_time += time.time() - start_time
            label.config(text=format_time(elapsed_time))

    def on_reset():
        nonlocal is_running, start_time, elapsed_time
        is_running = False
        start_time = None
        elapsed_time = 0.0
        label.config(text="0.00 seconds")

    def on_quit():
        global timer_popup
        nonlocal is_running
        is_running = False
        if timer_popup:
            timer_popup.destroy()
            timer_popup = None

    timer_popup.protocol("WM_DELETE_WINDOW", on_quit)

    btn_frame = tk.Frame(timer_popup, bg="#1E1E1E")
    btn_frame.pack(pady=4)

    btn_style = {
        "font": ("Helvetica", 12, "bold"),
        "bg": "#2D2D2D",
        "fg": "#E1E1E1",
        "activebackground": "#3E3E3E",
        "activeforeground": "#00E5FF",
        "borderless": 1,
        "padx": 8,
        "pady": 3,
    }

    buttons = [
        ("Start", on_start),
        ("Stop", on_stop),
        ("Reset", on_reset),
        ("Quit", on_quit),
    ]

    for text, cmd in buttons:
        btn = Button(btn_frame, text=text, command=cmd, **btn_style)
        btn.pack(side="left", padx=4)

    print("[NCTC] Floating timer opened.")
    timer_popup.mainloop()


def cmd_timer():
    open_timer_popup()


if __name__ == "__main__":
    cmd_timer()
