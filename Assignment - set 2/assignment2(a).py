from Order import *

if __name__ == '__main__':
    # adding items its price and weight to the catelogue
    i1 = Item("Soap", 20, 50)
    i2 = Item("Salt", 40, 2000)
    i3 = Item("Gold", 10, 52000)

    # Order Items and its quantity
    oi1 = OrderItem(i1, 5)
    oi2 = OrderItem(i2, 1)
    oi3 = OrderItem(i3, 2)

    # Placing the order
    o = Order("DemoPerson", 'Antilla, Altamount Road, Cumballa Hill, Mumbai.')
    o.order_item(oi1)
    o.order_item(oi2)
    o.order_item(oi3)
    
    # See the details of order
    o.__str__()