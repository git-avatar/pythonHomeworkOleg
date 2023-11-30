import random

transactions = []
transactions_num = int(input("how many transactions do u want"))
for i in range(transactions_num):
    year = random.randint(1950, 2023)
    month = random.randint(1, 12)
    day = random.randint(1, 30)
    description = random.choice([
        "This transaction is for a family",
        "This transaction is for an institution",
        "This transaction is for a company",
        "This transaction is for a personal business",
        "Sorry, this transaction doesn't have a description",
        "This transaction is for a restaurant",
        "This transaction is for a bank",
        "This transaction is for a charity"
    ])
    income = random.randint(1, 100000)
    expenses = random.randint(1, 100000)
    profit = income - expenses

    transaction = {
        "Year-Month-Day": [year, month, day],
        "Description": description,
        "Income": income,
        "Expenses": expenses,
        "Profit": profit
    }

    transactions.append(transaction)

print(transactions)

question = input("Do you know the index of your transaction?(Yes/No)")
if question == "Yes":
    transaction = int(input("Enter the number of the transaction you need(0-LastTransaction):"))
    print("Your transaction is:", transactions[transaction])
else:
    print("Enter your transaction")

year2 = int(input("Enter the year"))
month2 = int(input("Enter the month"))
day2 = int(input("Enter the day"))
income2 = int(input("Enter the income"))
expenses2 = int(input("Enter the expenses"))
profit2 = income2 - expenses2
description2 = str(input("Enter the description"))
index = transactions.index({"Year-Month-Day": [year2, month2, day2],"Description": description2,"Income": income2,"Expenses": expenses2,"Profit": profit2})

for transaction in transactions:
    if any({"Year-Month-Day": [year2, month2, day2],"Description": description2,"Income": income2,"Expenses": expenses2,"Profit": profit2}):
        print("Here's the index to your transaction:", index)
        specific_transaction = int(input("Enter the index for your transaction"))
        print("This is your transaction", transactions[specific_transaction])
for transaction in transactions:
    if not any({"Year-Month-Day": [year2, month2, day2],"Description": description2,"Income": income2,"Expenses": expenses2,"Profit": profit2}):
        print("Sorry, we don't have this particular transaction")
