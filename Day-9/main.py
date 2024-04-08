# programming_dictionary= {
#     "name" : "amol",
#     "age" : 21,
#     "college" : "hola university"
    
# }

# print(programming_dictionary)

# programming_dictionary["company"] = "fractal"

# print(programming_dictionary)

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


std_marks = {
    "amol" : 89,
    "anuja" : 95,
    "shubham" : 92,
    "bhushan": 91,
    "dummy" : 75,
    "anup" : 31,
    "shantaram"  : 70
}

std_grade = {

}

for student in std_marks:
    score = std_marks[student]

    if score>90:
        std_grade[student] = "Outstanding"
    elif score > 80:
        std_grade[student] = "exceeds exception"
    elif score > 70:
        std_grade[student] = "acceptable"
    else:
        std_grade[student] = "fail"

print(std_grade)