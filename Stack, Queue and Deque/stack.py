class Stack(object):

    def __init__(self):
        self._data = []
    # Fill out the Stack Methods here
    def is_empty(self):
        return len(self._data == 0)
    
    def push(self, item):
        self._data.push(item)

    def pop(self):
        self._data.pop()
    
    def peek(self):
        return self._data[-1]
    
    def size(self):
        return len(self._data)
    