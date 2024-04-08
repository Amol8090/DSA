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


# std_marks = {
#     "amol" : 89,
#     "anuja" : 95,
#     "shubham" : 92,
#     "bhushan": 91,
#     "dummy" : 75,
#     "anup" : 31,
#     "shantaram"  : 70
# }

# std_grade = {

# }

# for student in std_marks:
#     score = std_marks[student]

#     if score>90:
#         std_grade[student] = "Outstanding"
#     elif score > 80:
#         std_grade[student] = "exceeds exception"
#     elif score > 70:
#         std_grade[student] = "acceptable"
#     else:
#         std_grade[student] = "fail"

# print(std_grade)



# travelling_blog = [
#     {
#         "country" : "india",
#         "visited_city":["pune","solapur","kolhapur","nashik"],
#         "no_of city" : 10
#     },
#     {
#         "country" : "US/uk",
#         "visited_plces" : ["washigton","paris","london"],
#         "no_of_city" :9

#     }

# ]


# travelling_blog = {
#     "india" : {"cities_visited" : ["pune","nashik"],"total_visites":10},
#     "goa" :{"cities visited":["panji","madgaon"],"total_visited":12}
# }


import os

bid_details = {

}

def highest_bidder(bid_details):
    highest_bid=0
    winner=""
    for name in bid_details:
        bid_value=bid_details[name]
        if bid_value>highest_bid:
            highest_bid=bid_value
            winner=name
    print(f"The winner of bidding is {winner} with the height bid of {highest_bid}")


is_bidder=True

while is_bidder:
    name=input("enter name of bidder : ")
    bid=int(input("enter the bid price : "))
    bid_details[name] = bid
    # bid_details.append(curr_bid)
    forward=input("is there anybody left : ").lower()
    if forward == "no":
        is_bidder=False
        break
    else:
        os.system('cls')
        continue

highest_bidder(bid_details)