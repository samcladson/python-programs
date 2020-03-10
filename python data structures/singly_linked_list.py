class node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.next = None


class linkedList:
    def __init__(self):
        self.headval = None

    def getData(self):
        node = self.headval
        while node is not None:
            print(node.dataval, end=" ")
            node = node.next


if __name__ == "__main__":
    linked_list = linkedList()
    linked_list.headval = node('days')
    temp = linked_list.headval
    for i in range(7):
        new_node = node(input())
        temp.next = new_node
        temp = new_node
    linked_list.getData()
