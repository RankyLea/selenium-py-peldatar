user_age = input("How old are you?):  ")
drink_order = input("What would you like to drink?:  ")
for i in drink_order[ != 'beer' or 'coke']:
    print("We have only beer or coke!")

    if user_age < 18 and drink_order == 'beer':
        print("You are too young to drink spirit")
    elif user_age > 60 and drink_order == 'coke':
        print("Caffeine can raise your blood pressure")
    else:
        print("Here is your [drink_order]")
