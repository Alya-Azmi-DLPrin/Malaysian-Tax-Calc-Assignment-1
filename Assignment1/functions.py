# TAX CALC FUNCTIONS

# creating a space to save previously registered users so they can login again
import csv
import os

# saving the user info
def save_user_to_csv(user_id, ic_number, filename="users.csv"):
    file_exists = os.path.isfile(filename)
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["user_id", "ic_number"])  # The header row
        writer.writerow([user_id, ic_number])

# to read and load it into main
def load_users_from_csv(filename="users.csv"):
    users = {}
    if not os.path.isfile(filename):
        return users  # No users yet
    with open(filename, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            users[row["user_id"]] = row["ic_number"]
    return users

#Checking the user info
def verify_user(ic_number, password):
    if len(ic_number) != 12 or not ic_number.isdigit():
        return False
    return password == ic_number[-4:]

#Doing the tax thing
def calculate_tax(income, tax_relief):
    chargeable_income = income - tax_relief
    if chargeable_income <= 0:
        return 0

#Tax rates reference from https://www.hasil.gov.my/en/individual/individual-life-cycle/how-to-declare-income/tax-rate/
    if chargeable_income <= 5000:
        tax = 0
    elif chargeable_income <= 20000:
        tax = (chargeable_income-5000) * 0.01
    elif chargeable_income <= 35000:
        tax = (chargeable_income-20000) * 0.03 + 150 
    elif chargeable_income <= 50000:
        tax = (chargeable_income-35000) * 0.06 + 600
    elif chargeable_income <= 70000:
        tax = (chargeable_income-50000) * 0.11 + 1500
    elif chargeable_income <= 100000:
        tax = (chargeable_income-70000) * 0.19 + 3700
    elif chargeable_income <= 400000:
        tax = (chargeable_income-100000) * 0.25 + 9400
    elif chargeable_income <= 600000:
        tax = (chargeable_income-400000) * 0.26 + 84400
    elif chargeable_income <= 2000000:
        tax = (chargeable_income-600000) * 0.28 + 136400
    else:
        tax = (chargeable_income-2000000) * 0.30 + 528400
    
    return round(tax,2)



import pandas as pd
import os 

#saving income and tax data to a csv
def save_to_csv(data, filename):
    df = pd.DataFrame([data])
    if os.path.exists(filename):
        df.to_csv(filename, mode='a', header=False, index=False)
    else:
        df.to_csv(filename, mode='w', header=True, index=False)

# reading the csv file
def read_from_csv(filename):
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        print ("The file does not exist!")
        return None
    
