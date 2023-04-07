# Lab Professor: Michael

from control import OnlineStore

control = OnlineStore()

print("\n----------Welcome to our online store !----------\n")

while True:

    menu = input("1 - View product\n2 - Add item to cart\n3 - Remove item from cart\n4 - View confirmed "
                 "order\n5 - Exit\n")

    while int(menu) < 1 or int(menu) > 5:
        print("\nThat is not a valid option in the system, please try again\n")
        menu = input("1 - View product\n2 - Add item to cart\n3 - Remove item from cart\n4 - View confirmed "
                     "order\n5 - Exit\n")

    if int(menu) == 1:
        control.display_products()

    if int(menu) == 2:
        control.add_item()

    if int(menu) == 3:
        control.remove_item()

    if int(menu) == 4:
        control.view_confirmed_order()

    if int(menu) == 5:
        print("\nEnding the system...Goodbye!")
        exit()
