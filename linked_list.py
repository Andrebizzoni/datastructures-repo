import gc

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListIterator:
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

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        return LinkedListIterator(self.head)
    
    def addFront(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    
    def addEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def addAfter(self, prev_node_data, data):
        new_node = Node(data)
        current = self.head
        while current.next:
            if current.data == prev_node_data:
                new_node.next = current.next
                current.next = new_node
                return
            else:
                current = current.next
        print("Item is not in LinkedList")

    def popFront(self):
        temp = self.head.next
        self.head.next = None
        self.head = temp
        gc.collect()

    def popEnd(self):
        penultimate = self.head
        while penultimate.next.next:
            penultimate = penultimate.next
        penultimate.next = None
        gc.collect()
    
    def popNode(self, node_data):
        current = self.head
        if current.data == node_data:
            self.popFront()
            return
        while current.next:
            if current.next.data == node_data:
                current.next = current.next.next
                gc.collect()
                return
            else:
                current = current.next
        print("Item is not in LinkedList")

    def sort(self, reverse=False):
        while True:
            current = self.head
            no_swaps = True
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

    def max(self):
        max = self.head.data
        for item in self:
            if item > max:
                max = item    
        return max

    def min(self):
        min = self.head.data
        for item in self:
            if item < min:
                min = item
        return min