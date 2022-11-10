# Transaction.py
# Manipulation (CRUD) of cart items within a transaction


##
# Libraries
##
import tabulate # pretty printing tables
from itertools import count # creating unique id in classes


##
# Class definitions
##

class Transaction:
    """Represents one transaction within the system."""

    # Initiate a counter to get ID [1 ... n]
    counter = count(1)
    
    def __init__(self) -> None:
        """Initializing this class with only an empty cart."""
        self.id = next(Transaction.counter)
        self.cart = []


    def is_in_cart(self, name) -> bool:
        """Checks whether item is in the shopping cart."""

        result = False

        # Iterates all shopping cart: if found, return true
        for line_item in self.cart:
            if line_item.get("name").lower() == name.lower():
                result = True
                break

        return result


    def check_order(self) -> None:
        """Pretty prints the order as an ascii table."""
        print(f"Transaction number: {self.id}")
        print(f"Your cart:\n{self.cart}\n")


    def reset_transaction(self) -> None:
        """Resetting transaction by deleting all cart items."""
        self.cart = []
        print(f"Reset for transaction #{self.id} is successful. Your cart is now empty.\n")


    def add_item(self, name, qty, price) -> None:
        """Adding exactly one item to the shopping cart.
        
        Keyword arguments:
        name -- (string) name of the item
        qty -- (int) quantity of item
        price -- (float) price of one item
        """

        # Return error if arguments are of different type
        # TODO -- handle price data type
        if not (isinstance(name, str) and isinstance(qty, int)):
            print("System error: Failed to add new item.")
            print("Please check the input:")
            print("- Name should be text")
            print("- Quantity should be integer\n")

        # If quantity is 0, return error
        elif qty == 0:
            print("System error: Failed to add new item.")
            print("Cannot add item with 0 quantity.\n")
        
        # If duplicates, then return error
        elif self.is_in_cart(name) == True:
            print("System error: Failed to add new item.")
            print("An item with the same name is already in the system.")
            print("Please recheck name, or update the item instead.\n")
        
        # Add new item if there is no duplicate
        else:
            new_item = {
                "name": name,
                "qty": qty,
                "price": price
            }
            self.cart.append(new_item)
            print(f"{qty}x {name} has been added to the cart.\n")



##
# Module testing
##

if __name__ == "__main__":
    t = Transaction()
    t.add_item(name=100, qty="Tempe", price=100.00)
    t.add_item(name="Tempe", qty=0, price=100.00)
    t.add_item(name="Tempe", qty=100, price=100.00)
    t.check_order()
    t.reset_transaction()
    t.check_order()
