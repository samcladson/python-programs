class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        
class AddNode:
    def __init__(self):
        self.head = None
        
        
    def display(self):
        node = self.head
        while node is not None:
            print(node.data,end=" ")
            node = node.next
    def reverse(self):
        prev = None
        cur = self.head
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev
        
if __name__ == "__main__":
    l1 = AddNode()
    l1.head = node(1)
    l1.head.next = node(2)
    l1.head.next.next = node(3)
    l1.head.next.next.next = node(4)
    l1.display()
    l1.reverse()
    l1.display()