# class Node:
#     def __init__(self,dataval=None):
#         self.dataval = dataval
#         self.nextval = None

# class SLinkedList:
#     def __init__(self) -> None:
#         self.headval =None
#     # print linked list
#     def listprint(self):
#       printval = self.headval
#       while printval is not None:
#          print (printval.dataval)
#          printval = printval.nextval
    
#     def AtBeginning(self,newdata):
#         NewNode = Node(newdata)
    
#     # update the new nodes next val to exisiting
#         NewNode.nextval = self.headval
#         self.headval = NewNode
    

# list1 = SLinkedList()
# list1.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")
# list1.headval.nextval = e2
# e2.nextval = e3

# list1.AtBeginning("Sun")
# list1.listprint()

# class LinkedList:
#     def __init__(self,head=None) -> None:
#         self.head = head

#     def insert(self, value):
#         node = LinkedNode(value)
#         if self.head is None:
#             self.head = node
#             return
#         currentNode = self.head
#         while True :
#             if currentNode.nextNode is None:
#                 currentNode.nextNode = node
#                 break 
#             currentNode = currentNode.nextNode
    
#     def printLinkedList(self):
#         currentNode = self.head
#         while currentNode is not None:
#             print (currentNode.value, '->')
#             currentNode = currentNode.nextNode
#         print ("None")

# class LinkedNode:
#     def __init__(self,value,nextNode=None):
#         self.value = value
#         self.nextNode = nextNode

# node1 = LinkedNode("3")
# node2 = LinkedNode("4")
# node3 = LinkedNode("5")
# node4 = LinkedNode("6")

# node1.nextNode = node2 # node1 -> node2
# node2.nextNode = node3 # node2 -> node3

# currentNode = node1
# while True:
#     print (currentNode.value, "->")
#     if currentNode.nextNode is None:
#         print ("None")
#         break
#     currentNode = currentNode.nextNode


# linked list
# l1 = LinkedList()
# l1.printLinkedList()
# l1.insert("3")
# l1.printLinkedList()
# l1.insert("4")
# l1.printLinkedList()

class Node :
    def __init__(self,data) -> None:
        self.data= data
        self.next = None

class Sll:
    def __init__(self) -> None:
        self.head = None
    
    def traversal(self):
        if self.head is None:
            print("Singly linked list is empty")
        else:
            a= self.head
            while a is not None:
                print (a.data,end =" ")
                a = a.next

    def insert_at_beginning(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
    
    def insert_at_end(self,data):
        ne=Node(data)
        a = self.head
        while a.next is not None:
            a= a.next
        a.next=ne
    
    def insert_at_specified_node(self,postition,data):
        nib = Node(data)
        a = self.head
        for i in range(1,postition-1):
            a=a.next
            nib.next = a.next
            a.next = nib

sll = Sll()
n1=Node(5)
sll.head=n1
n2=Node(10)
n1.next=n2
n3=Node(15)
n2.next=n3
n4=Node(25)
n3.next=n4
n5=Node(30)
n4.next=n5

sll.insert_at_beginning(2)
sll.insert_at_end(25)
sll.insert_at_specified_node(3,7)
sll.traversal()

