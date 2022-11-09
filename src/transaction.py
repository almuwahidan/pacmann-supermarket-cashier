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


    def check_order(self) -> None:
        """Pretty prints the order as an ascii table."""
        print(f"Transaction number: {self.id}")
        print(f"Your cart:\n{self.cart}\n")


    def reset_transaction(self) -> None:
        """Resetting transaction by deleting all cart items."""
        self.cart = []
        print(f"Reset for transaction #{self.id} is successful. Your cart is now empty.\n")



##
# Module testing
##

if __name__ == "__main__":
    t = Transaction()
    t.check_order()
    t.reset_transaction()

    t = Transaction()
    t.check_order()
    t.reset_transaction()