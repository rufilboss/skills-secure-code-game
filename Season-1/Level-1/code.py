'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_ORDER_AMOUNT = 1e6  # A reasonable max order amount to prevent excessive values
EPSILON = 1e-9  # Define a small epsilon for floating-point comparison

def validorder(order: Order):
    total_payments = 0
    total_products = 0

    for item in order.items:
        if item.type == 'payment':
            total_payments += item.amount
        elif item.type == 'product':
            product_cost = item.amount * item.quantity
            total_products += product_cost
            # Check for total amount exceeding reasonable limit
            if total_products > MAX_ORDER_AMOUNT:
                return "Total amount payable for an order exceeded"
        else:
            return f"Invalid item type: {item.type}"

    # Compare total payments and total products considering floating-point precision
    if abs(total_payments - total_products) > EPSILON:
        return f"Order ID: {order.id} - Payment imbalance: ${total_payments - total_products:0.2f}"
    else:
        return f"Order ID: {order.id} - Full payment received!"