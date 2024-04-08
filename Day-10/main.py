def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2


operations = {
    "+" : sum,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

num1=int(input("Enter the first number : "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Enter which operation you wan to perform : ")
num2=int(input("Enter the second number : "))
calculation_function=operations[operation_symbol]
answer=calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")