import calendar
from datetime import datetime


def run_calendar():

    current_year = datetime.now().year

    cal_rules = (
        "\n [] Type a number <1-12> to see the month"
        "\n [] press <Enter> or any Letter to Exit"
    )

    print(f"<<<<<<< Welcome to NCTC Calendar! >>>>>>>: {cal_rules}")

    while True:
        try:
            usr_input = int(input("\n type months (1-12):"))

            if 1 <= usr_input <= 12:
                print()
                print(calendar.month(current_year, usr_input))
            else:
                print(f"\n invalid input, pls note the rules: {cal_rules} ")

        except ValueError:
            print("thank you for using NCTC Calendar")
            break


if __name__ == "__main__":
    run_calendar()
