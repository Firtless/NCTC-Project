# NCTC

from Note import notepad_cli
from Cal import run_calendar
from Time import cmd_timer
from Calc import calc_run


def run_nctc():

    nctc_rules = (
        "\n 1. [N] | NotePad | press < 1 > to access"
        "\n 2. [C] | Calendar | press < 2 > to access"
        "\n 3. [T] | Timer | press < 3 > to access"
        "\n 4. [C] | Calculator | press < 4 > to access"
        "\n 5. [Exit] to exit press Enter or any letter"
        "\n 6. [Rules] input any number bigger than 4"
    )

    print(f" \n <<<<<<< Welcome to NCTC APP! >>>>>>>: \n {nctc_rules}")

    while True:
        try:
            usr_input = int(input(" \n Enter your choice:"))

            if usr_input == 1:
                notepad_cli()
            elif usr_input == 2:
                run_calendar()
            elif usr_input == 3:
                cmd_timer()
            elif usr_input == 4:
                calc_run()
            else:
                print(f" \n Invalid input pls follow the rules: {nctc_rules}")
        except ValueError:
            print("\n thank you for using the NCTC app!!! \n")
            break


if __name__ == "__main__":
    run_nctc()
