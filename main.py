# Lab Professor: Michael

from data import Data

print("\n----------Welcome to our online store !----------\n")

while True:

    menu = input("1 - View product\n2 - Purchase item\n3 - Remove item from cart\n4 - Exit\n")

    while int(menu) < 1 or int(menu) > 4:
        print("\nThat is not a valid option in the system, please try again\n")
        menu = input("1 - View product\n2 - Purchase item\n3 - Remove item from cart\n4 - Exit\n")

    if int(menu) == 1:
        test = Data()
        print("\n********** PRODUCTS LISTS **********\n")
        for item in range(len(test.createData())):
            print(f"ID: {test.createData()[item][0]}")
            print(f"PRODUCT NAME: {test.createData()[item][1]}")
            print(f"PRICE: {test.createData()[item][2]}")
            print(f"CATEGORY: {test.createData()[item][3]}\n")

    if int(menu) == 2:
        print("2 works")

    if int(menu) == 3:
        print("3 works")

    if int(menu) == 4:
        print("\nEnding the system...good bye")
        exit()
