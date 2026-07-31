import time
import sys
import threading
from colorama import Fore, Style, init

init(autoreset=True)


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


def live_time(start_time, stop_event):

    while not stop_event.is_set():
        elapsed = time.time() - start_time

    sys.stdout.write(
        f'\r{Fore.CYAN} {format_time(elapsed)} {Style.RESET_ALL}')
    sys.stdout.flush()
    time.sleep(0.1)

    sys.stdout.write('\r' + ' ' * 40 + '\r')
    sys.stdout.flush()


def cmd_timer():
    print("<<< NCTC Timer >>>")
    print("Commands: 'start' to begin | 'stop' to end | 'exit' to quit")

    start = None
    start_time = None
    stop_event = None
    timer_thread = None

    while True:
        cmd_input = input("\nNCTC >").lower().strip()

        if cmd_input == "start":
            if timer_thread and timer_thread.is_alive():
                print("timer running")
                continue

            start = time.time()
            stop_event = threading.Event()

            timer_thread = threading.Thread(
                target=live_time,
                args=(start_time, stop_event),
                daemon=True,
            )

            timer_thread.start()

        elif cmd_input == "stop":

            if not timer_thread or not timer_thread.is_alive():
                print("No timer is currently running!")
                continue

            stop_event.set()
            timer_thread.join()

            final_elapsed = time.time() - start_time
            print(
                f"⏱️  Time elapsed: {Fore.GREEN}{format_time(final_elapsed)}{Style.RESET_ALL}"
            )
            start_time = None

            end = time.time()
            print(f"time elapsed: {end - start:.2f} seonds")

        elif cmd_input == "exit":
            print("thank u for using NCTC Timer!")
            break
        else:
            print("worng input! Please follow the Commands")


if __name__ == "__main__":
    cmd_timer()
