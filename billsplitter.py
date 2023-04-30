import random

print("Enter the number of friends joining (including you):")
count = int(input())
names = []

if count > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    while count > 0:
        count -= 1
        names.append(input())

    print("Enter the total bill value:")
    bill = int(input())

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    choice = input()
    split_count = len(names)
    lucky = None

    if choice == "Yes":
        split_count -= 1
        random.shuffle(names)
        lucky = names[0]
        print(f"{lucky} is the lucky one!")
    else:
        print("No one is going to be lucky")

    split_bill = round(bill / split_count, 2)
    party = dict.fromkeys(names, split_bill)

    if lucky is not None:
        party[lucky] = 0

    print(party)
else:
    print("No one is joining for the party")
