from Node import Node
from WGI_Groups import WGI


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, e):
        newNode = Node(e)

        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            current_last = self.tail
            current_last.setNext(newNode)
            newNode.setPrevious(current_last)
            self.tail = newNode

        self.size += 1

    def insert(self, index, object):
        newNode = Node(object)
        current = self.head

        if index == 0:
            current.setPrevious(newNode)
            newNode.setNext(current)
            self.head = newNode
        elif index == self.size - 1:
            newNode.setNext(self.tail)
            newNode.setPrevious(self.tail.getPrevious())
            self.tail.getPrevious().setNext(newNode)
            self.tail.setPrevious(newNode)
        elif index == self.size:
            current_last = self.tail
            current_last.setNext(newNode)
            newNode.setPrevious(current_last)
            self.tail = newNode
        else:
            for i in range(index):
                current = current.getNext()

            newNode.setNext(current)
            newNode.setPrevious(current.getPrevious())
            current.getPrevious().setNext(newNode)
            current.getNext().setPrevious(newNode)

        self.size += 1

    def delete(self, index):
        if index >= self.size or index < 0:
            return

        if self.size == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            self.head = self.head.getNext()
            self.head.setPrevious(None)
        elif index == self.size - 1:
            self.tail = self.tail.getPrevious()
            self.tail.setNext(None)
        else:
            current = self.head

            for index in range(index):
                current = current.getNext()

            current.getNext().setPrevious(current.getPrevious())
            current.getPrevious().setNext(current.getNext())

        self.size -= 1

    def length(self):
        return self.size

    def search(self, school):
        current = self.head

        while current is not None:
            if current.getData().get_school() == school:
                return current.getData()

            current = current.getNext()

    def __getitem__(self, index):
        current = self.head

        for i in range(index):
            current = current.getNext()

        return current.getData()

    def merge(self, a, b):
        newList = LinkedList()

        a_current = a.head
        b_current = b.head

        while a_current is not None and b_current is not None:
            if a_current.getData().get_score() > b_current.getData().get_score():
                newList.add(a_current.getData())
                a_current = a_current.getNext()
            else:
                newList.add(b_current.getData())
                b_current = b_current.getNext()

        while a_current is not None:
            newList.add(a_current.getData())
            a_current = a_current.getNext()

        while b_current is not None:
            newList.add(b_current.getData())
            b_current = b_current.getNext()

        return newList

    def mergeSort(self):
        if self.length() < 2:
            return self
        else:
            a = LinkedList()
            b = LinkedList()

            a_sorted = LinkedList()
            b_sorted = LinkedList()

            for i in range(self.length() // 2):
                a.add(self[i])

            for i in range(self.length() // 2, self.length()):
                b.add(self[i])

            a_sorted = a.mergeSort()
            b_sorted = b.mergeSort()

            return self.merge(a_sorted, b_sorted)

    def __str__(self):
        current = self.head
        stringToReturn = str(current)

        while current.getNext() is not None:
            current = current.getNext()
            stringToReturn = stringToReturn + "\n\n" + str(current)

        return stringToReturn

if __name__ == "__main__":
    Old_Bridge = WGI("Old Bridge", "World", 95, "11/15/20")
    Avon = WGI("Avon", "World", 96, "4/22/23")

    world_class = LinkedList()
    world_class.add(Old_Bridge)
    world_class.add(Avon)

    sorted_world = world_class.mergeSort()

    print(sorted_world)