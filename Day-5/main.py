# n=int(input("how many students"))
# lst=[]
# for i in range(0,n):
#     ele=int(input("enter height in cm "))
#     lst.append(ele)

# print(lst)
# sum=0
# for height in lst:
#     sum+=height

# print(f"average height of students is {sum/n}")


# highest=0
# for ele in lst:
#     if ele>highest:
#         highest=ele
    
# print(highest)


# for i in range(2,100,2):
#     print(i)


for i in range(0,100):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")

    else:
        print(i)