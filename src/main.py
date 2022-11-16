# main.py
# Main program which drives user interactions


##
# Imports
##
import os # for clear screen
from transaction import Transaction
import pdb


##
# Supporting functions
##
def clear_screen():
    """Clear terminal screen. Works for Windows and Unix-based OSes."""

    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def add_item(t_obj):
    """Interface to add item to the Transaction object.

    Arguments:
    t_obj -- (Transaction) instance from Transaction class.
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

    input("Press Enter to go back to main menu...")
    clear_screen()
    ##


def remove_item(t_obj):
    """Interface to remove one item from the Transaction object.

    Arguments:
    t_obj -- (Transaction) instance from Transaction class.
    """
    
    print("\n == Remove one item ==\n")
    t.check_order()
    name = input("Name of the item you'd like to delete: ")

    try:
        name = str(name)

        t.delete_item(name=name)

    except ValueError:
        print("App Error: Data type mismatch. Name should be alphanumeric.")

    input("Press Enter to go back to main menu...")
    clear_screen()
    ##


def update_item(t_obj):
    """Interface to  update one item from the Transaction object.

    Arguments:
    t_obj -- (Transaction) instance from Transaction class.
    """
    
    print("\n == Update one item ==\n")
    t.check_order()
    name = input("\nName of the item you'd like to update: ")
    option = None # option from users when picking the main menu

    # Check for name input data type
    try:
        name = str(name)
        line_item = t.get_item(name=name)
    except ValueError:
        print("App Error: Data type mismatch. Name should be alphanumeric.")

    clear_screen()

    # If item is found, get the data point users wish to change
    if line_item is not None:
        print("\n == Update one item ==\n")
        print(f"You picked {line_item['name']}.\n")
        print("You can change:")
        print("1. Name")
        print("2. Quantity")
        print("3. Price")

        # Call update functions depending on the option
        try:
            option = int(input("Choose the number correspoding with the menu: "))

            if option == 1:
                new_name = str(input("New item name: "))
                t.update_item_name(name=name, new_name=new_name)

            elif option == 2:
                new_qty = int(input("New item quantity: "))
                t.update_item_qty(name=name, new_qty=new_qty)

            elif option == 3:
                new_price = float(input("New item price: "))
                t.update_item_price(name=name, new_price=new_price)

            else:
                print("Option is unavailable.\n")

        except ValueError:
            print("The data you've inputted is wrong:")
            print("- Picking an option should use a number.")
            print("- Name should be a text.")
            print("- Quantity should be an integer.")
            print("- Price should be a float.\n")
        
    
    # if item is not found, print error
    else:
        print(f"Item {name} is not found.\n")

    input("Press Enter to go back to main menu...")
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
    pdb.set_trace()

    add_item(t)
    t.check_order()
    update_item(t)
    t.check_order()