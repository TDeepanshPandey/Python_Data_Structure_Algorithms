class Queue(object):
    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)
    
    def enqueue(self, item):
        self._data.append(item)
    
    def dequeue(self):
        self._data.pop(0)
    