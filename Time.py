import time
import sys
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


def time_animation(duration):
    end_time = time.time() + duration
    while True:
        time_remaining = end_time - time.time()

        if time_remaining <= 0:
            break

        sys.stdout.write(
            f'\r{Fore.CYAN} {format_time(time_remaining)} {Style.RESET_ALL}')
        sys.stdout.flush()
        time.sleep(0.1)


def cmd_timer():
    print("<<< NCTC Timer >>>")
    print("Commands: 'start' to begin | 'stop' to end | 'exit' to quit")

    start = None

    while True:
        cmd_input = input("\nNCTC >").lower().strip()

        if cmd_input == "start":
            start = time.time()
            time_animation(duration=3)

        elif cmd_input == "stop":
            end = time.time()
            print(f"time elapsed: {end - start:.2f} seonds")

        elif cmd_input == "exit":
            print("thank u for using NCTC Timer!")
            break
        else:
            print("worng input! Please follow the Commands")


if __name__ == "__main__":
    cmd_timer()
