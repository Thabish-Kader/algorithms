

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

    def delete_at_benginning(self):
        temp = self.head

        # Move the head pointer to the next node
        self.head = temp.next
        temp.next = None
    
    def delete_at_end(self):
        prev = self.head
        a = prev.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None

    def delete_at_pos(self,position):
        print()
        prev = self.head
        a = self.head.next
        for i in range(1,position-1):
            print(i)
            prev = prev.next
            a = a.next
            
        prev.next = a.next
        a.next = None






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
sll.traversal()
print()
sll.insert_at_beginning(2)
sll.traversal()
print()
sll.insert_at_end(25)
sll.traversal()
print()
sll.insert_at_specified_node(3,7)
sll.traversal()
print()
sll.delete_at_benginning()
sll.traversal()
print()
sll.delete_at_pos(3)
sll.traversal()

