class node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.next = None


class linkedList:
    def createHead(self):
        self.headval = None

    def getData(self):
        node = self.headval
        while node is not None:
            print(node.dataval)
            node = node.next

    def createAtBegining(self):
        for i in range(int(input('Enter range : '))):
            new_node = node(input())
            new_node.next = self.headval
            self.headval = new_node

    def createAtEnd(self):
        temp = self.headval
        for i in range(int(input('Enter your range : '))):
            new_node = node(input())
            temp.next = new_node
            temp = new_node

    def searchData(self):
        node = self.headval
        flag = 0
        search_data = input('\nEnter Search.. : ')

        while node is not None:
            if node.dataval == search_data:
                print("Data Fond : {}".format(node.dataval))
                break
            else:
                flag = 1
            node = node.next
        if flag == 1:
            print('Oops.. No data found.')


if __name__ == "__main__":
    linked_list = linkedList()
    linked_list.headval = node('data')
    choice = 0
    while choice != 5:
        print('\n1) CREATE At BEGINING\n2) CREATE AT END\n3) SEARCH \n4) DISPLAY \n')
        choice = int(input('Enter Your Choice : '))

        if choice == 1:
            linked_list.createAtBegining()
        if choice == 2:
            linked_list.createAtEnd()
        if choice == 3:
            linked_list.searchData()
        if choice == 4:
            linked_list.getData()
