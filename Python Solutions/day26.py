class List:
    head = None

    class Node:        
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        pass

    # method to add values to list
    def add(self, value):
        if self.head == None: # List not initiated
            self.head = self.Node(value)
        else: # List already initiated
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = self.Node(value)

    # method to find last K-th element from the list
    def lastKthElem(self, k):
        temp1 = self.head
        for i in range(k):
            temp1 = temp1.next
        
        temp2 = self.head
        while(temp1.next != None):
            temp1 = temp1.next
            temp2 = temp2.next

        return temp2.value


if __name__ == "__main__":
    # list construction
    linkedList = List()
    linkedList.add(43) # 6
    linkedList.add(17) # 5
    linkedList.add(10) # 4
    linkedList.add(38) # 3
    linkedList.add(21) # 2
    linkedList.add(62) # 1
    linkedList.add(32) # 0

    print("Last kth Element : ", linkedList.lastKthElem(3))