# Documentation: Supermarket Cashier System


## Background
The system is created to **assist users in listing down and calculating the prices of their shopping list**.

The objective above is broken down into different functionalities below:
![Functionalities](https://github.com/almuwahidan/pacmann-supermarket-cashier/blob/main/img/system-functionalities.png)


## Modules
This system consists of a few modules represented as Python files:
- `transaction.py` -- contains Transaction class: CRUD of shopping lists
- `payments.py` -- contains the logic for discount calculation
- `main.py` -- inputting and checking user commands, and calling the appropriate functions within the Transaction class.


## Implementation


### Program workflow
System-level workflow:
![System-level workflow](https://github.com/almuwahidan/pacmann-supermarket-cashier/blob/main/img/system-level-workflow.png)

Main menu workflow:
![Main-menu workflow](https://github.com/almuwahidan/pacmann-supermarket-cashier/blob/main/img/main-menu-workflow.png)


### Shopping list data structure
The shopping list is represented as a `list`, and each item is represented as a `dict` of:
- `name` -- representing the name of the item (string)
- `qty` -- representing quantity of said item in the cart (int)
- `price` -- representing the price of **one** quantity of the item (float)

This means the whole shopping list will look similar to this:

```python
    [
        {'name': 'Tempe', 'qty': 1, 'price': 10000.00},
        {'name': 'Sampo sachet', 'qty': 10, 'price': 1000.00}
    ]
```


### Attributes and Functions in Transaction class

Attributes in the Transaction class:
![List of Attributes](https://github.com/almuwahidan/pacmann-supermarket-cashier/blob/main/img/transaction-attributes.png)

Functions in the Transaction class:
![List of functions](https://github.com/almuwahidan/pacmann-supermarket-cashier/blob/main/img/transaction-functions.png)


## Demonstration
Can be shown at [demo.md](https://github.com/almuwahidan/pacmann-supermarket-cashier/blob/main/demo.md)