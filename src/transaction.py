# Transaction.py
# Manipulation (CRUD) of cart items within a transaction


##
# Libraries
##
import tabulate # pretty printing tables
from itertools import count # creating unique id in classes
from payments import calc_discount


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


    def calc_basket_price(self) -> float:
        """Calculate basket price before discounts."""
        
        # Variable to store prices
        basket_price = 0

        # Calculate basket price by iterating thru the cart
        for line_item in self.cart:
            basket_price += line_item.get("qty") * line_item.get("price")

        return basket_price


    def print_price_breakdown(self) -> None:
        """Prints total payable price of the shopping cart, after discounts."""
        
        basket_price = self.calc_basket_price()
        discount_price = calc_discount(basket_price)
        payable_price = basket_price - discount_price

        print("Your price breakdown:")
        print(f"Basket price: {basket_price}")
        print(f"Discount: {discount_price}")
        print(f"You pay: {payable_price}\n")


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
            print("App error: Failed to add new item.")
            print("Please check the input:")
            print("- Name should be text")
            print("- Quantity should be integer\n")

        # If quantity is 0, return error
        elif qty == 0:
            print("App error: Failed to add new item.")
            print("Cannot add item with 0 quantity.\n")
        
        # If duplicates, then return error
        elif self.is_in_cart(name) == True:
            print("App error: Failed to add new item.")
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


    def delete_item(self, name) -> None:
        """Delete an item from the shopping cart."""

        is_found = False

        # Return error if arguments are of different type
        if not isinstance(name, str):
            print("App error: Failed to remove item.")
            print("Please check the input: Name should be text.\n")

        # iterate thru the cart, delete first occurence of item
        else :
            for line_item in self.cart:

                if line_item.get("name").lower() == name.lower():
                    print(f"{line_item.get('qty')}x {line_item.get('name')} has been removed from the cart.\n")
                    self.cart.remove(line_item)
                    is_found = True
                    break

        # return error if item is not found
        if is_found == False:
            print(f"Delete item failed: {name} is not found.\n")



##
# Module testing
##

if __name__ == "__main__":
    t = Transaction()

    # # Test: adding items
    # print("== Add Item ==")
    # t.add_item(name=100, qty="Tempe", price=100.00)
    # t.add_item(name="Tempe", qty=0, price=100.00)
    # t.add_item(name="Tempe", qty=100, price=100.00)
    # t.add_item(name="Tempe", qty=1, price=100.00)
    # t.check_order()

    # # Test: delete item
    # print("== Delete Item ==")
    # t.add_item(name="Tahu", qty=10, price=100.00)
    # t.delete_item(name="Combro")
    # t.check_order()
    # t.delete_item(name="Tahu")
    # t.check_order()

    # # Test: reset order
    # t.add_item(name="Tempe", qty=100, price=100.00)
    # t.check_order()
    # t.reset_transaction()
    # t.check_order()

    # Test: payments
    t.add_item(name="Tempe", qty=1, price=200000)
    print("200k basket: 0 discount")
    t.print_price_breakdown()
    t.add_item(name="Tahu", qty=1, price=100000)
    print("300k basket: 0.05 discount")
    t.print_price_breakdown()
    t.add_item(name="Combro", qty=1, price=200000)
    print("500k basket: 0.08 discount")
    t.print_price_breakdown()
    t.add_item(name="Yoyoyo", qty=1, price=1)
    print("500k +1 basket: 0.1 discount")
    t.print_price_breakdown()
