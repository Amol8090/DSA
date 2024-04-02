# num=int(input("enter the number"))

# if num%2 ==0:
#     print("it's an even number")
# else:
#     print("its an odd number")

# print("calculatin the BMI")
# weight = int(input("enter the body weight in kg"))
# height = float(input("enter the height in meter"))
# bmi=int(weight/height**2)
# print(f"your bmi is {bmi}")


# if bmi < 18.5:
#     print(f"your bmi is {bmi} and you are underweight")
# elif 18.5<bmi<25:
#     print(f"you have nomrmal weight, your bmi is {bmi} ")
# else:
#     print("you are overweight")


# year = int(input("enter the year to check"))

# if (year % 4 ==0 and year % 100 !=0) or year%400==0:
#     print("its a leap year")
# else:
#     print("its not a leap year")

print("python pizza delivery")
size=input("size of the pizza(S,M,L)")
add_peporani = input("do you want paperoni(Y,N)")
extra_cheese = input("do you want extra cheese(Y,N)")

if size=='S':
    bill=15
    if add_peporani == 'Y':
        bill+=2
    if extra_cheese == 'Y':
        bill+=1

if size=='M':
    bill=20
    if add_peporani == 'Y':
        bill+=3
    if extra_cheese == 'Y':
        bill+=1

if size=='M':
    bill=25
    if add_peporani == 'Y':
        bill+=3
    if extra_cheese == 'Y':
        bill+=1

print(f"your bill is {bill}")