import gc

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedListIterator:
    def __init__(self, head):
        self.current = head
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next
            return item

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        return DoublyLinkedListIterator(self.head)
    
    def addFront(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def addEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
            new_node.prev = last
    
    def addAfter(self, prev_node_data, data):
        new_node = Node(data)
        current = self.head
        while current.next:
            if current.data == prev_node_data:
               new_node.next = current.next
               current.next.prev = new_node
               current.next = new_node
               new_node.prev = current
               return
            else:
                current = current.next
        return print("Item is not in DoublyLinkedList")

    def popFront(self):
        self.head.next.prev = None
        temp = self.head.next
        self.head.next = None
        self.head = temp
        gc.collect()

    def popEnd(self):
        penultimate = self.head
        while penultimate.next.next:
            penultimate = penultimate.next
        penultimate.next.prev = None
        penultimate.next = None
        gc.collect()

    def popNode(self, node_data):
        current = self.head
        if current.data == node_data:
            self.popFront()
            return
        while current.next:
            if current.data == node_data:
                previous = current.prev
                previous.next = current.next
                current.next.prev = previous
                current.prev = None
                current.next = None
                gc.collect
                return
            else:
                current = current.next
        if current.data == node_data:
            self.popEnd()
            return
        return print("Item is not in DoublyLinkedList")

    def sort(self, reverse=False):
        while True:
            no_swaps = True
            current = self.head
            while current.next:
                if reverse:
                    if current.data < current.next.data:
                        current.data, current.next.data = current.next.data, current.data
                        no_swaps = False
                elif current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    no_swaps = False
                current = current.next
            if no_swaps:
                return

    def min(self):
        min = self.head.data
        for item in self:
            if item < min:
                min = item
        return min

    def max(self):
        max = self.head.data
        for item in self:
            if item > max:
                max = item
        return max

list = DoublyLinkedList()
list.addFront(5)
list.addFront(10)
list.addEnd(9)
list.addEnd(4)
list.addAfter(9, 6)
list.sort(reverse=True)
for item in list:
    print(item)
