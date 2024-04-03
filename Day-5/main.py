n=int(input("how many students"))
lst=[]
for i in range(0,n):
    ele=int(input("enter height in cm "))
    lst.append(ele)

print(lst)
sum=0
for height in lst:
    sum+=height

print(f"average height of students is {sum/n}")