# for data scan usage
import os
# import class from file "data"
from data import Data


class OnlineStore:

    # initialize the variables that will be used in later function
    def __init__(self):
        self.cart_list = []
        self.cart_total = 0
        self.price = 0
        self.single_total = 0
        self.grand_total = 0
        self.order_num = 1
        self.store = Data()

    # display the information of the product from the database created: "final.db"
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

    # ask user to enter the id and quantity of the product to add it to the card
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

                        # search through the database to see if entered product id exists or not
                        status = "found"
                        self.price = int(self.store.createData()[loc][2])
                        name = self.store.createData()[loc][1]
                        id = self.store.createData()[loc][0]
                        category = self.store.createData()[loc][3]
                        break
                    elif not int(select_id) == int(self.store.createData()[loc][0]):
                        status = "unavailable"
                        continue
                # execute if entered id matches the one in the database
                if status == "found":
                    select_quantity = input("Please enter the quantity of the product you would like to purchase:\n")
                    while not select_quantity.isdigit():
                        print("Invalid input for quantity, please try again\n")
                        select_quantity = input(
                            "Please enter the quantity of the product you would like to purchase:\n")

                    # if quantity is over 10, apply 5% discounts to the price, and add the product info to the cart list
                    if int(select_quantity) >= 10:
                        self.single_total = (int(select_quantity) * self.price) * 0.95
                    else:
                        self.single_total = int(select_quantity) * self.price
                    self.cart_list.append([int(id), name, int(select_quantity), int(self.single_total), category])
                    self.cart_total += self.single_total

                    print("Your item has been added to the cart !\n")

                    cont = input("Would you like to add more items to your cart or proceed to order "
                                 "confirmation?\nPress Y/y to continue || N/n to proceed\n")

                    # exception handling
                    while not cont == "Y" and not cont == "y" and not cont == "N" and not cont == "n":
                        print("\nInvalid input, please try again")
                        cont = input("Would you like to add more items to your cart or proceed to order "
                                     "confirmation?\nPress Y/y to continue || N/n to proceed\n")

                    if cont == "Y" or cont == "y":
                        continue
                    if cont == "N" or cont == "n":
                        break

                # if entered id is not found, repeat the loop and ask the user to enter again
                if status == "unavailable":
                    print("Item with this ID doesn't exists, please try again\n")

        print("\n---------- ORDER CONFIRMATION ----------\n")

        # display order confirmation with data associated to each product
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

            # check if the total price is over 75, and apply shipping cost according to that and add tax for grand total
            if self.cart_total < 75:
                print("Shipping cost: Applied ($9.99)\n")
                self.grand_total = (9.99 + self.cart_total) * 1.13
            else:
                print("Shipping cost: Free\n")
                self.grand_total = self.cart_total * 1.13

            print(f"Grand Total (including tax): ${round(self.grand_total, 2)}")

            # write or create file if not exists and write all the confirmed purchase information into order.txt file
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

            # reset all the cart information once the purchase is finished
            self.grand_total = 0
            self.cart_total = 0
            self.cart_list = []

            cont = input("\nWould you like to go back to the menu ?\nPress Y/y for YES || N/n for NO\n")

            # exception handling
            while not cont == "Y" and not cont == "y" and not cont == "N" and not cont == "n":
                print("\nInvalid input, please try again")
                cont = input("\nWould you like to go back to the menu ?\nPress Y/y for YES || N/n for NO\n")

            if cont == "Y" or cont == "y":
                return
            if cont == "N" or cont == "n":
                exit()

        if finalize == "N" or finalize == "n":
            return

    # ask the user to enter the id of the product that they want to remove from the cart
    def remove_item(self):
        # display if the cart is empty
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

                # shows all the current list of the product that is in the cart
                for item in range(len(self.cart_list)):
                    print(f"PRODUCT ID: {self.cart_list[item][0]}")
                    print(f"PRODUCT NAME: {self.cart_list[item][1]}")
                    print(f"QUANTITY: {self.cart_list[item][2]}\n")

                remove = input("Please enter the ID of the product the you would like to remove from the cart")

                while not remove.isdigit():
                    print("Invalid input, please try again")
                    remove = input("\nPlease enter the ID of the product the you would like to remove from the cart")

                # search through the cart list to see if entered product id exists or not
                for item in range(len(self.cart_list)):
                    if int(remove) == int(self.cart_list[item][0]):
                        status = "found"
                        id = self.cart_list[item][0]
                        loc = int(item)
                        break
                    elif not int(remove) == int(self.cart_list[item][0]):
                        status = "unavailable"
                        continue
                # if the entered id matches, ask user for confirmation and remove item from the cart list
                if status == "found":
                    confirm = input(
                        f"\nWould you like to confirm to remove product ID: '{id}' from your cart?\nPress Y/y to "
                        f"proceed || N/n to go back to menu")

                    # exception handling
                    while not confirm == "Y" and not confirm == "y" and not confirm == "N" and not confirm == "n":
                        print("\nInvalid input, please try again")
                        confirm = input(
                            f"\nWould you like to confirm to remove product ID: '{id}' from your cart?\nPress Y/y to "
                            f"proceed || N/n to go back to menu")

                    if confirm == "y" or confirm == "Y":
                        # remove item from cart
                        self.cart_list.pop(loc)
                        print(f"\nItem ID: {id} has been removed from your cart!")
                        back = input("\nPress any button to go back to menu")
                        break
                    if confirm == "n" or confirm == "N":
                        break

                # if entered id is not found, repeat the loop and ask the user to enter again
                if status == "unavailable":
                    print("\nThere is no item with this ID in your cart, please try again")

    def view_confirmed_order(self):
        # create file if not exists, unless the file data is empty, show the information of confirmed purchase
        create = open("order.txt", "a+")
        file = open("order.txt", "r")
        # check if the data of the file is empty or not
        if os.path.getsize("order.txt") == 0:
            print("There is no confirmed order yet!")
        else:
            print("\n***** List of confirmed order *****\n")
            print(file.read())
        back = input("\nEnter any button to return to menu: ")
        if back:
            return
