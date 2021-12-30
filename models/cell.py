class Cell:
    def __init__(self, x, y, head=False, body=False, tail=False, food=False):
        self._x = x
        self._y = y
        self.head = head
        self.body = body
        self.tail = tail
        self.food = food

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y