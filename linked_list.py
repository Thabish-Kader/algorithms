class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self) -> None:
        self.headval =None
    # print linked list
    def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
    
    def AtBeginning(self,newdata):
        NewNode = Node(newdata)
    
    # update the new nodes next val to exisiting
        NewNode.nextval = self.headval
        self.headval = NewNode
    

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list1.headval.nextval = e2
e2.nextval = e3


list1.AtBeginning("Sun")
list1.listprint()
