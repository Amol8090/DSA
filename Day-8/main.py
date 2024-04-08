###functions
import math
def greet():
    print("hello")
    print("how are you?")
    print("how was oyur day?")

greet()


def greet_with_name(name):
    print(f"hello {name}")

greet_with_name("amol")

def greet_with(name,location):
    print(f"hello {name}, are you in {location}")

greet_with("amol","pune")


def calculate(height,width):
    return (height*width)/5

paint=math.ceil(calculate(2,4))
print(paint)


def prime_number(num):
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
    if is_prime:
        print("it's a prime number")
    else:
        print("it's not a prime number")

number = 11

prime_number(number)