class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []

    def push(self, number):
        if not self.items:
            self.items.append((number, number))
        else:
            smallestVal = number
            smallestVal = min(smallestVal, self.items[-1][1])
            self.items.append((number, smallestVal))

    def pop(self):
        return self.items.pop()[0]

    def top(self):
        return self.items[-1][0]

    def getMin(self):
        return self.items[-1][1]


if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())
