import os
from data import Data


class OnlineStore:

    def __init__(self):
        self.cart_list = []
        self.cart_total = 0
        self.price = 0
        self.single_total = 0
        self.grand_total = 0
        self.order_num = 1
        self.store = Data()

    def display_products(self):
        print("\n********** PRODUCTS LISTS **********\n")
        for item in range(len(self.store.createData())):
            print(f"ID: {self.store.createData()[item][0]}")
            print(f"PRODUCT NAME: {self.store.createData()[item][1]}")
            print(f"PRICE: {self.store.createData()[item][2]}")
            print(f"CATEGORY: {self.store.createData()[item][3]}\n")
        back = input("\nEnter any button to return to menu: ")
        if back:
            return

    def add_item(self):
        while True:
            select_id = input("Please enter the ID of the product you would like to add to the cart: ")
            status = ""
            name = ""
            id = 0
            category = ""

            if not select_id.isdigit():
                print("Invalid input for product ID, please try again\n")
            else:
                for loc in range(len(self.store.createData())):
                    if int(select_id) == int(self.store.createData()[loc][0]):
                        status = "found"
                        self.price = int(self.store.createData()[loc][2])
                        name = self.store.createData()[loc][1]
                        id = self.store.createData()[loc][0]
                        category = self.store.createData()[loc][3]
                        break
                    elif not int(select_id) == int(self.store.createData()[loc][0]):
                        status = "unavailable"
                        continue
                if status == "found":
                    select_quantity = input("Please enter the quantity of the product you would like to purchase:\n")
                    while not select_quantity.isdigit():
                        print("Invalid input for quantity, please try again\n")
                        select_quantity = input(
                            "Please enter the quantity of the product you would like to purchase:\n")
                    if int(select_quantity) >= 10:
                        self.single_total = (int(select_quantity) * self.price) * 0.95
                    else:
                        self.single_total = int(select_quantity) * self.price
                    self.cart_list.append([int(id), name, int(select_quantity), int(self.single_total), category])
                    self.cart_total += self.single_total

                    print("Your item has been added to the cart !\n")

                    cont = input("Would you like to add more items to your cart or proceed to order "
                                 "confirmation?\nPress Y/y to continue || N/n to proceed\n")

                    while not cont == "Y" and not cont == "y" and not cont == "N" and not cont == "n":
                        print("\nInvalid input, please try again")
                        cont = input("Would you like to add more items to your cart or proceed to order "
                                     "confirmation?\nPress Y/y to continue || N/n to proceed\n")

                    if cont == "Y" or cont == "y":
                        continue
                    if cont == "N" or cont == "n":
                        break

                if status == "unavailable":
                    print("Item with this ID doesn't exists, please try again\n")

        print("\n---------- ORDER CONFIRMATION ----------\n")

        for item in range(len(self.cart_list)):
            print(f"PRODUCT ID: {self.cart_list[item][0]}")
            print(f"PRODUCT NAME: {self.cart_list[item][1]}")
            if self.cart_list[item][2] >= 10:
                print(f"QUANTITY: {self.cart_list[item][2]} - 5% discount applied")
            else:
                print(f"QUANTITY: {self.cart_list[item][2]}")
            print(f"Total: ${self.cart_list[item][3]}\n")

        print(f"Grand Total (before tax): ${round(self.cart_total, 2)}")

        finalize = input(
            "\nWould you like to confirm your purchase ?\nPress Y/y for YES || N/n to go back to menu\n")

        while not finalize == "Y" and not finalize == "y" and not finalize == "N" and not finalize == "n":
            print("\nInvalid input, please try again")
            finalize = input(
                "\nWould you like to confirm your purchase ?\nPress Y/y for YES || N/n to go back to menu\n")

        if finalize == "Y" or finalize == "y":
            print("\nThank you for your purchase ! Your order has been confirmed")
            print("\n---------- RECEIPT ----------\n")

            for item in range(len(self.cart_list)):
                print(f"PRODUCT ID: {self.cart_list[item][0]}")
                print(f"PRODUCT NAME: {self.cart_list[item][1]}")
                print(f"QUANTITY: {self.cart_list[item][2]}\n")

            if self.cart_total < 75:
                print("Shipping cost: Applied ($9.99)\n")
                self.grand_total = (9.99 + self.cart_total) * 1.13
            else:
                print("Shipping cost: Free\n")
                self.grand_total = self.cart_total * 1.13

            print(f"Grand Total (including tax): ${round(self.grand_total, 2)}")

            file = open("order.txt", "a+")
            file.write(f"----- ORDER NUMBER: {self.order_num} -----\n")
            for item in range(len(self.cart_list)):
                file.write(f"PRODUCT ID: {self.cart_list[item][0]}\n")
                file.write(f"PRODUCT NAME: {self.cart_list[item][1]}\n")
                file.write(f"QUANTITY: {self.cart_list[item][2]}\n")
                file.write(f"Total: ${self.cart_list[item][3]}\n\n")
            file.write(f"GRAND TOTAL: ${round(self.grand_total, 2)}\n\n")
            file.close()
            self.order_num += 1
            self.grand_total = 0
            self.cart_total = 0
            self.cart_list = []

            cont = input("\nWould you like to go back to the menu ?\nPress Y/y for YES || N/n for NO\n")

            while not cont == "Y" and not cont == "y" and not cont == "N" and not cont == "n":
                print("\nInvalid input, please try again")
                cont = input("\nWould you like to go back to the menu ?\nPress Y/y for YES || N/n for NO\n")

            if cont == "Y" or cont == "y":
                return
            if cont == "N" or cont == "n":
                exit()

        if finalize == "N" or finalize == "n":
            return

    def remove_item(self):
        if len(self.cart_list) == 0:
            print("\nThere is no item in the cart yet !\n")
            back = input("\nPress any button to go back to menu")
            if back:
                return
        else:
            while True:
                status = ""
                id = 0
                loc = 0

                print("Items on your cart:\n")

                for item in range(len(self.cart_list)):
                    print(f"PRODUCT ID: {self.cart_list[item][0]}")
                    print(f"PRODUCT NAME: {self.cart_list[item][1]}")
                    print(f"QUANTITY: {self.cart_list[item][2]}\n")

                remove = input("Please enter the ID of the product the you would like to remove from the cart")

                while not remove.isdigit():
                    print("Invalid input, please try again")
                    remove = input("\nPlease enter the ID of the product the you would like to remove from the cart")

                for item in range(len(self.cart_list)):
                    if int(remove) == int(self.cart_list[item][0]):
                        status = "found"
                        id = self.cart_list[item][0]
                        loc = int(item)
                        break
                    elif not int(remove) == int(self.cart_list[item][0]):
                        status = "unavailable"
                        continue
                if status == "found":
                    confirm = input(
                        f"\nWould you like to confirm to remove product ID: '{id}' from your cart?\nPress Y/y to "
                        f"proceed || N/n to go back to menu")

                    while not confirm == "Y" and not confirm == "y" and not confirm == "N" and not confirm == "n":
                        print("\nInvalid input, please try again")
                        confirm = input(
                            f"\nWould you like to confirm to remove product ID: '{id}' from your cart?\nPress Y/y to "
                            f"proceed || N/n to go back to menu")

                    if confirm == "y" or confirm == "Y":
                        self.cart_list.pop(loc)
                        print(f"\nItem ID: {id} has been removed from your cart!")
                        back = input("\nPress any button to go back to menu")
                        break
                    if confirm == "n" or confirm == "N":
                        break

                if status == "unavailable":
                    print("\nThere is no item with this ID in your cart, please try again")

    def view_confirmed_order(self):
        create = open("order.txt", "a+")
        file = open("order.txt", "r")
        if os.path.getsize("order.txt") == 0:
            print("There is no confirmed order yet!")
        else:
            print("\n***** List of confirmed order *****\n")
            print(file.read())
        back = input("\nEnter any button to return to menu: ")
        if back:
            return
