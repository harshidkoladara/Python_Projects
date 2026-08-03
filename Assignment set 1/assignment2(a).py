from Order import *

if __name__ == '__main__':
    # adding items its price and weight to the catelogue
    i1 = Item("Perfume", 2000, 120)
    i2 = Item("Shampoo", 150, 80)
    i3 = Item("Wine", 10000, 3000)

    # Order Items and its quantity
    oi1 = OrderItem(i1, 4)
    oi2 = OrderItem(i2, 10)
    oi3 = OrderItem(i3, 2)

    # Placing the order
    o = Order("Admin", '1600, Pennsylvania Avenue NW, Washington, D.C. 20500, U.S.')
    o.order_item(oi1)
    o.order_item(oi2)
    o.order_item(oi3)
    
    # See the details of order
    o.__str__()