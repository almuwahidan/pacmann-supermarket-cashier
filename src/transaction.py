# Transaction.py
# Manipulation (CRUD) of cart items within a transaction


##
# Libraries
##

from tabulate import tabulate # pretty printing tables
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
        ##


    def is_in_cart(self, name) -> bool:
        """Checks whether item is in the shopping cart."""

        result = False

        # Iterates all shopping cart: if found, return true
        for line_item in self.cart:
            if line_item.get("name").lower() == name.lower():
                result = True
                break

        return result
        ##


    def get_item_index(self, name) -> int:
        """Get a line item's index within the shopping cart.
        
        return idx -- (int) index of item in the list. If item is not found, return None.
        """
        
        idx = None

        # iterate thru the cart to find the item
        for line_item in self.cart:
            if line_item.get("name").lower() == name.lower():
                idx = self.cart.index(line_item)
                break

        return idx
        ##


    def get_item(self, name) -> dict:
        """Gets item object given the name of the item.
        
        return item -- (dict) dictionary containing 'name', 'qty', 'price' of a line item. None if not found.
        """

        item_found = None

        # iterate thru the cart to find the item
        for line_item in self.cart:
            if line_item.get("name").lower() == name.lower():
                item_found = line_item

        return item_found
        ##


    def calc_basket_price(self) -> float:
        """Calculate basket price before discounts."""
        
        # Variable to store prices
        basket_price = 0

        # Calculate basket price by iterating thru the cart
        for line_item in self.cart:
            basket_price += line_item.get("qty") * line_item.get("price")

        return basket_price
        ##


    def print_price_breakdown(self) -> None:
        """Prints total payable price of the shopping cart, after discounts."""
        
        basket_price = self.calc_basket_price()
        discount_price = calc_discount(basket_price)
        payable_price = basket_price - discount_price

        print("Your price breakdown:")
        print(f"Basket price: {basket_price}")
        print(f"Discount: {discount_price}")
        print(f"You pay: {payable_price}\n")
        ##


    def check_order(self) -> None:
        """Pretty prints the order as a table."""

        header = [{'#': '#', 'name': 'Name', 'qty': 'Qty', 'price': 'Price per qty'}]
        cart_copy = self.cart.copy()
        i = 1

        for line_item in cart_copy:
            line_item['#'] = i
            i += 1

        lst = header + cart_copy

        # Print list contents if not empty
        if len(cart_copy) != 0:
            print(f"Transaction number: {self.id}")
            print("Your cart:")
            print(tabulate(lst, headers='firstrow', tablefmt='fancy_grid'))

        # If cart is empty, give notification
        else:
            print("Your cart is empty.\n")
        ##


    def reset_transaction(self) -> None:
        """Resetting transaction by deleting all cart items."""
        self.cart = []
        print(f"Reset for transaction #{self.id} is successful. Your cart is now empty.\n")
        ##


    def add_item(self, name, qty, price) -> None:
        """Adding exactly one item to the shopping cart.
        
        Keyword arguments:
        name -- (string) name of the item
        qty -- (int) quantity of item
        price -- (float) price of one item
        """

        # Return error if arguments are of different type
        if not (isinstance(name, str)
                and isinstance(qty, int)
                and (isinstance(price, float) or isinstance(price, int))):
            raise ValueError("Data type mismatch.")

        # If quantity is 0, return error
        elif qty == 0:
            print("App error: Failed to add new item.")
            print("Cannot add item with 0 quantity.\n")
        
        # If duplicates, then return error
        elif self.is_in_cart(name) == True:
            print(f"App error: Failed to add new item {name}.")
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


    def delete_item(self, name) -> None:
        """Delete a line item from the shopping cart."""

        is_found = False

        # Return error if arguments are of different type
        if not isinstance(name, str):
            raise ValueError("Data type mismatch.")

        # Deletes the item if found
        elif self.get_item_index(name) is not None:
            item = self.cart.pop(self.get_item_index(name))
            print(f"{item['qty']}x {item['name']} has been removed from the cart.\n")

        # Return error if item is not found
        else:
            print(f"Delete item failed: {name} is not found.\n")
        ##


    def update_item_name(self, name, new_name) -> None:
        """Update a line item's name within the shopping cart."""

        # Check arguments data types
        if not (isinstance(name, str) and isinstance(new_name, str)):
            raise ValueError("Data type mismatch.")

        # Updates item name if found
        elif self.get_item_index(name) is not None:
            self.cart[self.get_item_index(name)]['name'] = new_name
            print(f"Item {name}'s name has been changed to {new_name}.\n")
            
        # Return error if item is not found
        else:
            print(f"Item {name} is not found.")
            print("Please recheck name you've inputted.\n")
        ##
            

    def update_item_qty(self, name, new_qty) -> None:
        """Update a line item's quantity within the shopping cart."""

        # Check arguments data types
        if not (isinstance(name, str) and isinstance(new_qty, int)):
            raise ValueError("Data type mismatch.")

        # TODO -- handle quantity < 1

        # Updates item quantity if found
        elif self.get_item_index(name) is not None:
            self.cart[self.get_item_index(name)]['qty'] = new_qty
            print(f"Item {name}'s quantity has been changed to {new_qty}.\n")
            
        # Return error if item is not found
        else:
            print(f"Item {name} is not found.")
            print("Please recheck name you've inputted.\n")
        ##


    def update_item_price(self, name, new_price) -> None:
        """Update a line item's quantity within the shopping cart.
        argument new_price -- (int or float) new price set by user.
        """

        # Check arguments data types
        if not (isinstance(name, str) and (isinstance(new_price, int) or isinstance(new_price, float))):
            raise ValueError("Data type mismatch.")

        # Return error if new price <= 0
        elif new_price < 0.1:
            print("App error: Failed to update item price.")
            print("Item price cannot be lower than 0.1\n")

        # Updates item price if found
        elif self.get_item_index(name) is not None:
            self.cart[self.get_item_index(name)]['price'] = round(new_price*1.0, 2)
            print(f"Item {name}'s price has been changed to {new_price}.\n")
            
        # Return error if item is not found
        else:
            print(f"Item {name} is not found.")
            print("Please recheck name you've inputted.\n")
        ##


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
    # t.add_item(name="Tempe", qty=10, price=100.00)
    # t.add_item(name="Beras", qty=10, price=100.00)
    # t.delete_item(name="Combro")
    # t.check_order()
    # t.delete_item(name="Tempe")
    # t.check_order()

    # # Test: reset order
    # t.add_item(name="Tempe", qty=100, price=100.00)
    # t.check_order()
    # t.reset_transaction()
    # t.check_order()

    # # Test: payments
    # t.add_item(name="Tempe", qty=1, price=200000)
    # print("200k basket: 0 discount")
    # t.print_price_breakdown()
    # t.add_item(name="Tahu", qty=1, price=100000)
    # print("300k basket: 0.05 discount")
    # t.print_price_breakdown()
    # t.add_item(name="Combro", qty=1, price=200000)
    # print("500k basket: 0.08 discount")
    # t.print_price_breakdown()
    # t.add_item(name="Yoyoyo", qty=1, price=1)
    # print("500k +1 basket: 0.1 discount")
    # t.print_price_breakdown()

    # # Test: Update name
    # t.add_item(name="Tempe", qty=1, price=200000)
    # t.check_order()
    # t.update_item_name(name=100, new_name="Tempeeeee")
    # t.update_item_name(name="Tempe", new_name=100)
    # t.update_item_name(name="Tempeh", new_name="Tempeeeee")
    # t.update_item_name(name="Tempe", new_name="Tempeeeee")
    # t.check_order()

    # # Test: Update quantity
    # t.add_item(name="Tempe", qty=1, price=200000)
    # t.check_order()
    # t.update_item_qty(name=100, new_qty=100)
    # t.update_item_qty(name="Tempe", new_qty="Tempe")
    # t.update_item_qty(name="Tempe", new_qty=100)
    # t.update_item_qty(name="Tempe", new_qty=0)
    # t.check_order()

    # # Test: Update price
    t.add_item(name="Tempe", qty=1, price=200000)
    # t.check_order()
    # t.update_item_price(name=100, new_price=100)
    # t.update_item_price(name="Tempe", new_price="Tempe")
    # t.update_item_price(name="Tempe", new_price=100)
    # t.check_order()
    # t.update_item_price(name="Tempe", new_price=100.00)
    # t.update_item_price(name="Tempe", new_price=0)
    # t.check_order()
    # t.update_item_price(name="Tempe", new_price=0.1)
    # t.check_order()

