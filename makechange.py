coin_values = {
    "penny": 1,
    "nickel": 5,
    "dime": 10,
    "quarter": 25
}

operator_choice = ""
status = ""
amount = 0

user_entry = float(input("\nEnter number dollar amount as decimal... \n$")) * 100

# while status != "done":
    user_money = round(user_entry)

    print("\nYour change is:")

    # quarters
    print(str(int(user_money / coin_values["quarter"])) + " quarters")
    user_money = int(user_money % coin_values["quarter"])

    # dimes
    print(str(int(user_money / coin_values["dime"])) + " dimes")
    user_money = int(user_money % coin_values["dime"])

    # nickels
    print(str(int(user_money / coin_values["nickel"])) + " nickels")
    user_money = int(user_money % coin_values["nickel"])

    # pennies
    print(str(int(user_money / coin_values["penny"])) + " pennies")

    # ask what user would like to do next
    operator_choice = input("Choose (add) or (sub) or (done): ").lower()

    # logic to add, subtract or exit the application
    if operator_choice == "add":
        print(user_entry)
        amount = float(input("Enter Amount in decimal... \n$")) * 100
        user_entry = user_entry + round(amount)
    elif operator_choice == "sub":
        amount = float(input("enter Amount in decimal...\n$")) * 100
        user_entry = user_entry - round(amount)
    elif operator_choice == "done":
        print("\nGoodbye!\n")
        status = "done"
    else:
        print("An error has occured")
        status = "done"
