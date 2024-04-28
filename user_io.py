from integral_methods import *
from improper_integral_methods import *


def get_input():
    try:
        return input("$ ").strip().replace(",", ".")
    except (EOFError, KeyboardInterrupt):
        close_application_appropriately()


def close_application_appropriately():
    print("\nClosing application...")
    exit()


def launch():
    hello = "Computational Mathematics Lab 3: Integrals"
    print("-"*len(hello))
    print(hello)
    print("-" * len(hello))
    print()
    start()


def start():
    show_available_functions()
    while True:
        ans = get_input()
        if ans not in ["1", "2", "3", "4", "5"]:
            print("Please, choose one of the available functions.")
        else:
            break
    n = int(ans)
    parameters = get_integral_parameters()
    if n < 4:
        start_integral(n, parameters)
    else:
        start_improper_integral(n, parameters)


def start_integral(n, parameters):
    show_available_methods()
    while True:
        ans = get_input()
        if ans not in ["1", "2", "3"]:
            print("Please, choose one of the available methods.")
        else:
            break
    m = int(ans)
    methods = [left_rectangles, right_rectangles, middle_rectangles, trapezoid, simpson]
    result = methods[m - 1](n, parameters)
    show_integral_result(result)
    return


def get_integral_parameters():
    parameters = [0, 0, 0]
    print("Enter left integration boundary.")
    while True:
        ans = get_input()
        try:
            parameters[0] = float(ans)
        except ValueError:
            print("Please, enter a decimal number.")
            continue
        break
    print("Enter right integration boundary.")
    while True:
        ans = get_input()
        try:
            parameters[1] = float(ans)
        except ValueError:
            print("Please, enter a decimal number.")
            continue
        if parameters[1] < parameters[0]:
            print("Right boundary has to be greater than the left one.")
        else:
            break
    print("Enter calculation proximity (between 0 and 1).")
    while True:
        ans = get_input()
        try:
            parameters[2] = float(ans)
        except ValueError:
            print("Please, enter a decimal number.")
            continue
        if parameters[2] <= 0 or parameters[2] >= 1:
            print("Proximity has to be in range between 0 and 1.")
        else:
            break
    return parameters


def show_integral_result(result):
    print(f"Calculated value: {result[0]}")
    print(f"Total number of intervals: {result[1]}")


def start_improper_integral(n, parameters):
    result = solve_improper_integral(n, parameters)
    if result[0]:
        print(f"Calculated value: {result[1]}")
    else:
        print("Integral does not converge.")


def show_available_functions():
    print("Choose one of the available functions:")
    print("""2x^3 - 3x^2 + 5x - 9\t(1)
-x^3 - x^2 - 2x + 1\t\t(2)
4x^3 - 3x^2 + 5x - 20\t(3)
Functions for calculating improper integrals:
---\t(4)
---\t(5)""")


def show_available_methods():
    print("Choose one of the available methods:")
    print("""Left rectangles\t\t(1)
Right rectangles\t(2)
Middle rectangles\t(3)
Trapezoid\t\t\t(4)
Simpson\t\t\t\t(5)""")
