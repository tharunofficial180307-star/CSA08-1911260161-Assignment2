"""Q5: College Canteen Order System – Mutable Default Bug, Return Values, and Scope."""

def add_item_buggy(item, order=[]):
    order.append(item)
    return order

def add_item(item, order=None):
    # TODO 1 Completed
    if order is None:
        order = []
    order.append(item)
    return order

def calculate_bill(items, gst_rate=0.05):
    subtotal = sum(price for _, price in items)
    gst = round(subtotal * gst_rate, 2)
    return subtotal, gst, round(subtotal + gst, 2)

def make_order_tracker(customer_name):
    cart = []
    def add(item, price):
        nonlocal cart
        cart.append((item, price))
        return list(cart)
    return add

if __name__ == "__main__":
    print(add_item_buggy("Tea"), add_item_buggy("Vada"))
    print("Buggy __defaults__:", add_item_buggy.__defaults__)
    print(add_item("Tea"), add_item("Vada"))
    sub, tax, tot = calculate_bill([("Tea", 15.0), ("Vada", 20.0)])
    print(f"Bill -> Subtotal: {sub}, GST: {tax}, Total: {tot}")
