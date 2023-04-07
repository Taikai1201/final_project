# Lab Professor: Michael

# import class from file "control"
from control import OnlineStore

# set the class as a variable
control = OnlineStore()

print("\n----------Welcome to our online store !----------\n")

while True:

    menu = input("1 - View product\n2 - Add item to cart\n3 - Remove item from cart\n4 - View confirmed "
                 "order\n5 - Exit\n")

    # exception handling
    while int(menu) < 1 or int(menu) > 5:
        print("\nThat is not a valid option in the system, please try again\n")
        menu = input("1 - View product\n2 - Add item to cart\n3 - Remove item from cart\n4 - View confirmed "
                     "order\n5 - Exit\n")

    if int(menu) == 1:
        # View available product
        control.display_products()

    if int(menu) == 2:
        # Add item to the cart
        control.add_item()

    if int(menu) == 3:
        # Remove item from the cart
        control.remove_item()

    if int(menu) == 4:
        # Display the confirmed order of the user
        control.view_confirmed_order()

    if int(menu) == 5:
        print("\nEnding the system...Goodbye!")
        exit()
