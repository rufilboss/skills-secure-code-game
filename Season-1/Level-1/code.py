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

MAX_ORDER_AMOUNT = 1e6  # max order amount to prevent excessive values

def validorder(order: Order):
    net = 0
    total_product_amount = 0

    for item in order.items:
        if item.type == 'payment':
            net += item.amount
        elif item.type == 'product':
            product_cost = item.amount * item.quantity
            net -= product_cost
            total_product_amount += product_cost
            # Check for total amount exceeding reasonable limit
            if total_product_amount > MAX_ORDER_AMOUNT:
                return "Total amount payable for an order exceeded"
        else:
            return f"Invalid item type: {item.type}"

    # Check for unrealistic values that might trick the system
    if abs(net) > total_product_amount:
        return f"Order ID: {order.id} - Payment imbalance: ${net:0.2f}"
    
    if net != 0:
        return f"Order ID: {order.id} - Payment imbalance: ${net:0.2f}"
    else:
        return f"Order ID: {order.id} - Full payment received!"


# from collections import namedtuple

# Order = namedtuple('Order', 'id, items')
# Item = namedtuple('Item', 'type, description, amount, quantity')

# def validorder(order: Order):
#     net = 0

#     for item in order.items:
#         if item.type == 'payment':
#             net += item.amount
#         elif item.type == 'product':
#             net -= item.amount * item.quantity
#         else:
#             return "Invalid item type: %s" % item.type

#     if net != 0:
#         return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
#     else:
#         return "Order ID: %s - Full payment received!" % order.id