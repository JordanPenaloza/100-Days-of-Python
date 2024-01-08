
def prompt():
    
    a = int(input("First number: "))
    operation = input("Operation (+ - * /): ")
    b = int(input("Second number: "))
    func = operations[operation]
    answer = func(a, b)
    print(answer)


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

prompt()