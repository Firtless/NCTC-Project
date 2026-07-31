import time
import tkinter as tk
from tkmacosx import Button

timer_popup = None


def format_time(seconds):
    whole_seconds = int(seconds)
    milliseconds = seconds - whole_seconds

    minutes, secs = divmod(whole_seconds, 60)
    hours, mins = divmod(minutes, 60)

    if hours > 0:
        return f"{hours}h {mins}m {secs + milliseconds:.2f}s"
    elif mins > 0:
        return f"{mins}m {secs + milliseconds:.2f}s"
    else:
        return f"{seconds:.2f} seconds"


def open_timer_popup():
    global timer_popup

    if timer_popup is not None and timer_popup.winfo_exists():
        timer_popup.lift()
        return

    start_time = [None]
    elapsed_time = [0.0]
    is_running = [False]

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
        if is_running[0] and timer_popup.winfo_exists():
            current_elapsed = elapsed_time[0] + (time.time() - start_time[0])
            label.config(text=format_time(current_elapsed))
            timer_popup.after(100, tick)

    def on_start():
        if not is_running[0]:
            is_running[0] = True
            start_time[0] = time.time()
            tick()

    def on_stop():
        if is_running[0]:
            is_running[0] = False
            elapsed_time[0] += time.time() - start_time[0]
            label.config(text=format_time(elapsed_time[0]))

    def on_reset():
        is_running[0] = False
        start_time[0] = None
        elapsed_time[0] = 0.0
        label.config(text="0.00 seconds")

    def on_quit():
        global timer_popup
        is_running[0] = False
        if timer_popup:
            timer_popup.destroy()
            timer_popup = None

    timer_popup.protocol("WM_DELETE_WINDOW", on_quit)

    btn_frame = tk.Frame(timer_popup, bg="#1E1E1E")
    btn_frame.pack(pady=4)

    btn_style = {
        "font": ("Helvetica", 12, "bold"),
        "bg": "#2D2D2D",
        "fg": "#A4A4A4",
        "activebackground": "#3E3E3E",
        "activeforeground": "#00E5FF",
        "borderless": 1,
        "padx": 8,
        "pady": 3,
    }

    start_btn = Button(btn_frame, text="Start",
                       command=on_start, **btn_style)
    start_btn.pack(side="left", padx=4)

    stop_btn = Button(btn_frame, text="Stop", command=on_stop, **btn_style)
    stop_btn.pack(side="left", padx=4)

    reset_btn = Button(btn_frame, text="Reset",
                       command=on_reset, **btn_style)
    reset_btn.pack(side="left", padx=4)

    quit_btn = Button(btn_frame, text="Quit", command=on_quit, **btn_style)
    quit_btn.pack(side="left", padx=4)

    print("[NCTC] Floating timer opened.")
    timer_popup.mainloop()


def cmd_timer():
    open_timer_popup()


if __name__ == "__main__":
    cmd_timer()
