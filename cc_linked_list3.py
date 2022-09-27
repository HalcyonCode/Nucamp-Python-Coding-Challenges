""" Add a method called prepend() to the LinkedList class, with two parameters: self and value. 
The following two instructions can be handled in an identical way as in the append() method:
This method should instantiate a new object of the Node class, using the value passed in.
If the self object does not have a head attribute, assign the new Node object you just instantiated as the head, and print the message "Head Node created: " followed by the value of the node.
For the case in which the self object already has a head Node, you will then write code to assign the new Node object as the new head.
The existing head must then be linked to the new head. 
Afterward, print the message "Prepended new Head Node with value:" followed by the new head node's value.
Also print the message "Node following Head is:" followed by the value of the node referenced by the new head node's next attribute.
 """

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)
            return
        
        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Appended new Node with value:", node.next.value)

llist = LinkedList()
llist.append("First Node")
llist.append("Second Node")
llist.append("Third Node")