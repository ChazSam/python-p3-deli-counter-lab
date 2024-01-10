katz_deli = []

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        customers = [f"{i}. {name}" for i, name in enumerate(katz_deli, start = 1)]
        print("The line is currently: " + " ".join(customers))


def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        del katz_deli[0]
