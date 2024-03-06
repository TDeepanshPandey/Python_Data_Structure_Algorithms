class Deque(object):
    def __init__(self):
        self._data = []
    
    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def add_rear(self, item):
        self._data.append(item)

    def add_front(self,item):
        self._data.insert(0, item)

    def remove_rear(self):
        return self._data.pop()
    
    def remove_front(self):
        return self._data.pop(0)