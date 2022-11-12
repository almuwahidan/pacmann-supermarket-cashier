# main.py
# Main program which drives user interactions


##
# Imports
##
import os # for clear screen
from transaction import Transaction

##
# Supporting functions
##
def clear_screen():
    """Clear terminal screen. Works for Windows and Unix-based OSes."""

    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def add_item(t_obj):
    """Interface to add item to the Transaction object.

    argument t_obj -- (Transaction) instance from Transaction class.
    """
    
    print("\n== Add a new item ==")
    
    name = input("Item name: ")
    qty = input("Quantity: ")
    price = input("Price per quantity: ")

    try:
        name = str(name)
        qty = int(qty)
        price = float(price)

        print("\nResult:")
        t_obj.add_item(name=name, qty=qty, price=price)

    except ValueError:
        print("App Error: Data type mismatch. Please check your inputs.")
        print("- Name should be alphanumeric")
        print("- Quantity should be integer")
        print("- Price should be integer or float\n")

    input("Press Enter to continue...")
    clear_screen()
    ##


##
# Main menu function
##


##
# Main program
##

if __name__ == "__main__":
    t = Transaction()

    add_item(t)
    t.check_order()