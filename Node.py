class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.previous = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def setPrevious(self, previous):
        self.previous = previous

    def getPrevious(self):
        return self.previous

    def __str__(self):
        return str(self.getData())
