from datetime import datetime

#class Order
class Order:
    # Cunstructor for inintialization
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.timestamp = datetime.now()
        self.status = "Order Placed"
        self.price = 0
        self.weight = 0
        self.order_items = []        

    # for ordering the item
    def order_item(self, ordered_item):
        self.order_items.append(ordered_item)
        self.price += ordered_item.item.price * ordered_item.quantity
        self.weight += ordered_item.item.weight * ordered_item.quantity

    # show the details about all the orders    
    def __str__(self):
        print(f"Name: {self.name}\nAddress: {self.address}\nTotal Cost: {self.price}\nTotal Weight: {self.weight}\nOrder Time: {self.timestamp}")
        print("Ordered Items")
        for i, x in enumerate(self.order_items):
            print(f"\t{i+1}). {x.item.name}, Price: {x.item.price}, Weight: {x.item.weight}, Quantity: {x.quantity}, Total Weight: {x.quantity * x.item.weight}, Total Price: {x.quantity * x.item.price}")
        

# class OrderItem
class OrderItem:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity


# class Item
class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight