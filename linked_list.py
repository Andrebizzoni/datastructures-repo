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
        tmp = self.head.next
        self.head.next = None
        self.head = tmp

    def popEnd(self):
        penultimate = self.head
        while penultimate.next.next:
            penultimate = penultimate.next
        penultimate.next = None
    
    def popNode(self, node_data):
        current = self.head
        while current.next:
            if current.data == node_data:
                self.popFront()
                return
            elif current.next.data == node_data:
                current.next = current.next.next
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
        current = self.head
        max = self.head.data
        while current.next:
            if current.next.data > max:
                max = current.next.data
            current = current.next     
        return max

    def min(self):
        current = self.head
        min = self.head.data
        while current.next:
            if current.next.data < min:
                min = current.next.data
            current = current.next     
        return min


new_list = LinkedList()
new_list.addFront(1)
new_list.addFront(5)
new_list.addFront(10)
new_list.addEnd(0)
new_list.addEnd(100)
new_list.addAfter(5, 103)
new_list.popFront()
new_list.addEnd(15)

for item in new_list:
    print(item)

print("\n")
new_list.sort(reverse=True)

for item in new_list:
    print(item)

