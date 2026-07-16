# NCTC
# Procedural Programing \ Functoinal Programing

def get_num(text_input):

    while True:
        user_input = input(text_input).strip()

        if user_input.lower() == "exit":
            return "exit"

        try:
            return float(user_input)
        except ValueError:
            print(
                "wrong input! pls try again... but if u wish to finsish calculations type: exit")


def calc_task(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error. Cannot devide by zero"
        return num1 / num2
    else:
        return None


def calc_run():
    calc_count = 0
    print("<<< NCTC Calculator Initialized (Type 'exit' at any prompt to quit) >>>")

    while True:
        num1 = get_num("\n Enter your first number: ")
        if num1 == "exit":
            break

        num2 = get_num("\n Enter your secont number: ")
        if num2 == "exit":
            break

        operation = input("Choose action (+, -, *, /): ").strip()
        if operation.lower() == "exit":
            break

        result = calc_task(num1, num2, operation)

        if result is not None:
            print(f"Result: {result}")
            calc_count += 1
        else:
            print("!!! Wrong input, pls try again,  !!!")

    print(
        f"\n=== Session Closed. Total successful calculations: {calc_count} ===")


if __name__ == "__main__":
    calc_run()
