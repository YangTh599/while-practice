# Thayer Yang
#  10 DEC 2024
# While Loop Practice

from time import sleep as slp

# 7-4 Pizza Toppings

# toppings = []

# run = True

# while run:
#     topping = input("Enter a topping (Type \"-q-\" to quit):\n")
#     if topping == "-q-":
#         run = False

#     else:
#         if topping.isalpha() and not topping in toppings:
#             print(f"You added {topping} to your pizza!")
#             toppings.append(topping)
#             slp(.5)

#         elif not topping.isalpha():
#             print("Please enter only alphabetical characters")
#             slp(1)

#         elif topping in toppings:
#             print(f"You already have {topping} on your pizza!")
#             slp(2)
#     print()
    
# tops_str = ""
# for topping in toppings:
#     tops_str += (topping+", ")

# print("Here's what's on your pizza: "+tops_str[0:len(tops_str)-2])

# 7-5 Movie Tickets

# def check_tickets(tickets):
#     infants = 0
#     kids = 0
#     adults = 0
#     for ticket in tickets:
#         if ticket == 0:
#             infants+=1
#         elif ticket == 10:
#             kids+=1
#         elif ticket == 15:
#             adults +=1

#     str = f""">3 Tickets: {infants}
# 3-12 Tickets: {kids}
# 12< Tickets: {adults}"""
#     return str

# def check(answer):
#     if answer in ["y","ye","yes"]:
#         return True
#     elif answer in ["n","no","nope"]:
#         return False
#     else:
#         print("Please enter \"y\" or \"n\"!")

# ticket_prices = [10, 15]
# tickets_bought = []

# run = True
# while run:
#     buy = True

#     age = int(input("Please enter your age:\n"))
#     if age >=0 and age <3:
#         print("Your ticket is free!")
#         tickets_bought.append(0)
#     elif age >= 3 and age <=12:
#         print(f"Your ticket is ${ticket_prices[0]}")
#         tickets_bought.append(ticket_prices[0])
#     elif age > 12:
#         print(f"Your ticket is ${ticket_prices[1]}")
#         tickets_bought.append(ticket_prices[1])
#     else:
#         print("Invalid age")
    
#     while buy:
#         check = input("Would you like to buy another ticket? (y/n): ")
#         if check in ["y","ye","yes"]:
#             buy = False
#         elif check in ["n","no","nope"]:
#             buy = False
#             run = False
#         else:
#             print("Please enter \"y\" or \"n\"!")
#     print()

# print("Here are your tickets")
# print(check_tickets(tickets_bought))

# 7 - 6 Three exits: 7-4 Pizza toppings


# Flag Variable
toppings = []

run = True
while run:
    topping = input("Enter a topping (Type \"-q-\" to quit):\n")
    if topping == "-q-":
        run = False

    else:
        if topping.isalpha() and not topping in toppings:
            print(f"You added {topping} to your pizza!")
            toppings.append(topping)
            slp(.5)

        elif not topping.isalpha():
            print("Please enter only alphabetical characters")
            slp(1)

        elif topping in toppings:
            print(f"You already have {topping} on your pizza!")
            slp(2)
    print()
    
tops_str = ""
for topping in toppings:
    tops_str += (topping+", ")

print("Here's what's on your pizza: "+tops_str[0:len(tops_str)-2])

# Counter Variable

toppings = []

print("Enter 5 toppings.")
while len(toppings) < 5:
    topping = input("Enter a topping:\n")
    if topping.isalpha() and not topping in toppings:
        print(f"You added {topping} to your pizza!")
        toppings.append(topping)
        slp(.5)

    elif not topping.isalpha():
        print("Please enter only alphabetical characters")
        slp(1)

    elif topping in toppings:
        print(f"You already have {topping} on your pizza!")
        slp(2)
    print()
    
tops_str = ""
for topping in toppings:
    tops_str += (topping+", ")

print("Here's what's on your pizza: "+tops_str[0:len(tops_str)-2])

# Break Key Word

toppings = []

run = True
while run:
    topping = input("Enter a topping (Type \"-q-\" to quit):\n")
    if topping == "-q-":
        break

    else:
        if topping.isalpha() and not topping in toppings:
            print(f"You added {topping} to your pizza!")
            toppings.append(topping)
            slp(.5)

        elif not topping.isalpha():
            print("Please enter only alphabetical characters")
            slp(1)

        elif topping in toppings:
            print(f"You already have {topping} on your pizza!")
            slp(2)
    print()
    
tops_str = ""
for topping in toppings:
    tops_str += (topping+", ")

print("Here's what's on your pizza: "+tops_str[0:len(tops_str)-2])
