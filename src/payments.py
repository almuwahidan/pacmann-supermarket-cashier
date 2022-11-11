# Pricing.py
# Any additional logic before payment/checkout


##
# Functions
##

def calc_discount(basket_price) -> float:
    """Calculating discount based on the total basket price."""

    # TODO -- data type check; only accepts float or int

    # Initialize discount percentage
    pct_discount = 0.0

    # Determine discount percentage
    if basket_price > 500000:
        pct_discount = 0.1
    elif basket_price > 300000:
        pct_discount = 0.08
    elif basket_price > 200000:
        pct_discount = 0.05
    
    return round(basket_price*pct_discount, 2)