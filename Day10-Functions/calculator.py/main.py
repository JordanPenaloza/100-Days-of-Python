from art import logo
def calculator():
    
    print(logo)
    a = float(input("First number: "))
    should_continue = True

    while should_continue:

        operation = input("Operation (+ - * /): ")
        b = float(input("Second number: "))
        func = operations[operation]
        answer = func(a, b)
        print(answer)
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit, or type 'start' to start a new calculator:")
        if choice == "y":
            a = answer
        elif choice == "start":
            calculator()
        else:
            should_continue = False

def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b



operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
    
}
calculator()