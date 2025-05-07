#connect main w function
from functions import verify_user, calculate_tax, save_to_csv, read_from_csv, save_user_to_csv, load_users_from_csv

registered_users = load_users_from_csv()  # Load users from file
# print (registered_users) || Used during testing to see if the users were saved

print("Welcome to the Malaysian Tax Input Program")
print("This program is designed to help Malaysians calculate and update their tax amounts.")

user_status = input("Are you a new user? (yes/no): ").strip().lower()
# registration
if user_status == "yes":
    user_id = input("Register a user ID: ").strip()
    ic_number = input("Enter your 12-digit IC number (without dashes): ").strip()
    registered_users[user_id] = ic_number
    save_user_to_csv(user_id, ic_number)

    print("The registration is complete. Please proceed to log in.")
    print(" ")
    user_id = input("Enter your user ID: ")
    password = input("Enter your password (the last 4 digits of your IC): ")

    ic_number = registered_users.get(user_id, "")
#log in
else:
    user_id = input("Enter your user ID: ")
    password = input("Enter your password (the last 4 digits of your IC): ")

    ic_number = registered_users.get(user_id, "")
# failed login
if not verify_user(ic_number, password):
    print("Login failed. IC or password incorrect.")
    print("Exiting program. Please reopen program to start again.\n")
    input()
    exit()
# success login
print("Login successful.\n")

# asking for income and tax relief data
while True:
    try:
        income = float(input("Enter your annual income (RM): "))
        tax_relief = float(input("Enter your total tax relief (RM): "))
        break
    except ValueError:
        print("Invalid input. Please enter valid numbers for income and tax relief.")

#calculate and print
tax_payable = calculate_tax(income, tax_relief)
print(f"\n Tax payable: RM{tax_payable}")

user_data = {
    "IC Number": ic_number,
    "Income": income,
    "Tax Relief": tax_relief,
    "Tax Payable": tax_payable
}
# saving to csv
save_to_csv(user_data, "citizen_tax_records.csv")
print("Your data has been saved to citizen_tax_records.csv")

view_records = input("Would you like to see all past tax records? (y/n): ").lower()
# reading csv
if view_records == 'y':
    df = read_from_csv("citizen_tax_records.csv")
    if df is not None:
        print("\n [All Past Tax Records]")
        print(df)
    else:
        print("No records found.")

print("May this information be useful. \n Exiting Program...")