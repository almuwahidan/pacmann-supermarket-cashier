# Demo: Supermarket Cashier System

This is the demo of the system, based on test scenarios created by Pacmann team.

## Adding item

The customer wants to add
- `Ayam Goreng` x2; each have 20k price
- `Pasta Gigi` x3; each have 15k price

As the shopping cart is a `list` and item is a `dict`, we use this bit of code to add the items:

```python
    new_item = {
        "name": name,
        "qty": qty,
        "price": price
    }
    self.cart.append(new_item) # Append the list with the new item
```

![Adding the second item to the cart](https://github.com/almuwahidan/pacmann-supermarket-cashier/blob/main/img/add-item-1-input.png)

![Result in the cart page after addition](https://github.com/almuwahidan/pacmann-supermarket-cashier/blob/main/img/add-item-2-result.png)


## Deleting item

The customer wants to delete `Pasta Gigi`.

We're using this bit of code to delete the item

```python
    # If item is found, then delete the item from the cart

    elif self.get_item_index(name) is not None:
        item = self.cart.pop(self.get_item_index(name))
        print(f"{item['qty']}x {item['name']} has been removed from the cart.\n")
```

![Deleting Pasta Gigi from the cart](https://github.com/almuwahidan/pacmann-supermarket-cashier/blob/main/img/remove-item-1-input.png)

![Result in the cart page after deletion](https://github.com/almuwahidan/pacmann-supermarket-cashier/blob/main/img/remove-item-2-result.png)


## Reset transaction (wipe all items from the cart)

Wiping all items from the cart is simpler at this stage -- we just assign an empty list:

```python
    self.cart = []
    print(f"Reset for transaction #{self.id} is successful. Your cart is now empty.\n")
```

![Wiping all items from the cart](https://github.com/almuwahidan/pacmann-supermarket-cashier/blob/main/img/wipe-cart-1-input.png)

![Result in the cart page after wiping all items](https://github.com/almuwahidan/pacmann-supermarket-cashier/blob/main/img/wipe-cart-2-result.png)


## Calculate total price

The customer wants to calculate total price with these items:
- `Ayam Goreng` x2; each have 20k price
- `Pasta Gigi` x3; each have 15k price
- `Mainan Mobil` x1; each have 200k price
- `Mie Instan` x5; each have 3k price

Expected price is 285k after discounts.

We do this using this bit of code:

```python
    basket_price = self.calc_basket_price()
    discount_price = calc_discount(basket_price) # the logic is stored in payments.py
    payable_price = basket_price - discount_price

    print("Your price breakdown:")
    print(f"Basket price: {basket_price}")
    print(f"Discount: {discount_price}")
    print(f"You pay: {payable_price}\n") 
```

![Shopping cart for 4 line items](https://github.com/almuwahidan/pacmann-supermarket-cashier/blob/main/img/check-price-1-cart.png)

![Checking price for 4 line items](https://github.com/almuwahidan/pacmann-supermarket-cashier/blob/main/img/check-price-2-result.png)