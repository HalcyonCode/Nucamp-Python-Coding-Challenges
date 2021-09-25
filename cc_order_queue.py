""" Below the Queue class definition, define another class named IceCreamShop as follows:
class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()
You will write three methods for this class: take_order(), show_all_orders(), and next_order().
For the take_order() method, you will pass in 3 arguments aside from self: customer, flavor, and scoops. 
Assume that the customer and flavor arguments will be strings, and scoops will be an integer.
Write code to validate that the flavor string passed in exists in the self.flavors list, and that the scoops integer is between 1 and 3 inclusive, and show an appropriate error message if not.
Assuming validation went well and we have a valid order, print "Order created!".
Declare a variable named order. Assign as its value a dictionary that contains three keys, "customer", "flavor", and "scoops". For their values, use the arguments that were passed. 
Enqueue this order dictionary to the self.orders queue. 
For the show_all_orders() method, print all orders in the self.orders queue in a formatted way. See the Testing section below for the format. (Tip: You can use a for loop to format the orders as shown.)
For the next_order() method, dequeue the head order in the queue and show it. See the Testing section below for the format. 


Testing
Add the following testing code to the bottom of the file:
shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
This test code creates an IceCreamShop instance/object named shop using a list of ice cream flavors that is passed in.
Then, it takes four orders. The first and second orders have valid values. The third and fourth orders do not (invalid flavor, then invalid number of scoops).
Then, it shows all pending orders (the first and second). 
Then, it dequeues and displays the next order that should be fulfilled (the first one in).
Then, it shows all pending orders again (which should now have only one order left). 
 """

class Queue:
    def __init__(self):
        self.items = []
     
    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)
    
    def show_queue(self):
        print(self.items)

class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()
    
    def take_order(self, customer, flavor, scoops):
        self.customer = customer
        self.flavor = flavor
        self.scoops = scoops

        if (flavor in self.flavors) and (scoops in range(1, 4)):
            print("Order created!")
            order = {"customer": self.customer, "flavor": self.flavor, "scoops": self.scoops}
            self.orders.enqueue(order)
        elif flavor not in self.flavors:
            print("Sorry, we don't have that flavor")
        elif scoops not in range(1, 4):
            print("Choose between 1-3 scoops")

    def show_all_orders(self):
        print("\nAll Pending Ice Cream Orders:")
        for order in self.orders.items:
            print("Customer:", order["customer"],"--Flavor:", order["flavor"], "--Scoops:", order["scoops"])  
    
    def next_order(self):
        print("\nNext Order Up!")
        self.orders.dequeue
        print(self.orders.dequeue()) 

shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()