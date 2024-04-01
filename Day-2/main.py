# num = "12"

# a=int(num[0])
# b=int(num[1])
# print(a+b)

# print("calculatin the BMI")
# weight = int(input("enter the body weight in kg"))
# height = float(input("enter the height in meter"))

# bmi=int(weight/height**2)

# print(f"your bmi is {bmi}")

# print("calculating the weeks left")
# age=int(input("enter the age ib years"))
# const=90

# print(f"you have {(const-age)*52} weeks left ")


print("welcome to tip calculator")
bill= float(input("enter the total bill "))
tip_percentage = int(input("enter the percentage of tip"))
person = int(input("how many people are there "))
tip = round(((bill * tip_percentage)/100),2)

print(f"split of each person is {round(((bill+tip)/person),2)} ")
