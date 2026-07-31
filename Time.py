import time
import tkinter as tk
import threading
from colorama import Fore, Style, init

init(autoreset=True)

timer_popup = None

root = None
label = None
start_time = None
is_running = False


def format_time(seconds):
    whole_seconds = int(seconds)
    milliseconds = seconds - whole_seconds

    minuts, secs = divmod(whole_seconds, 60)
    hours, mins = divmod(minuts, 60)

    if hours > 0:
        return f"{hours}h {mins}m {secs + milliseconds:.2f}s"
    elif mins > 0:
        return f"{mins}m {secs + milliseconds:.2f}s"
    else:
        return f"{seconds:.2f} seconds"


def open_popup(start_time):
    global timer_popup
    timer_popup = tk.Tk()
    timer_popup.title("NCTC Timer")
    timer_popup.geometry("260x90")
    timer_popup.attributes("-topmost", True)
    timer_popup.configure(bg="#1E1E1E")

    label = tk.Label(
        timer_popup,
        text="0.00 seconds",
        font=("Helvetica", 18, "bold"),
        fg="#00E5FF",
        bg="#1E1E1E",
    )

    label.pack(expand=True)

    def tick():
        if timer_popup:
            elapsed = time.time() - start_time
            label.config(text=format_time(elapsed))
            timer_popup.after(100, tick)

    tick()
    timer_popup.mainloop()


def cmd_timer():
    print("<<< NCTC Timer >>>")
    print("Commands: 'start' to begin | 'stop' to end | 'exit' to quit")

    start = None

    while True:
        cmd_input = input("\nNCTC >").lower().strip()

        if cmd_input == "start":
            if start is not None:
                print("Timer is active!")
                continue

            start = time.time()
            threading.Thread(
                target=open_popup,
                args=(start,),
                daemon=True
            ).start()
            print("Timer started in floating window")

        elif cmd_input == "stop":
            if start is None:
                print("No timer is active!")
                continue

            end = time.time()
            print(
                f"Time elapsed: {Fore.GREEN}{format_time(end - start)}{Style.RESET_ALL}"
            )

            if timer_popup:
                timer_popup.destroy()
                timer_popup = None
            start = None

        elif cmd_input == "exit":
            if timer_popup:
                timer_popup.destroy()
            print("thank u for using NCTC Timer!")
            break
        else:
            print("worng input! Please follow the Commands")


if __name__ == "__main__":
    cmd_timer()
