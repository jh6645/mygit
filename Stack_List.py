class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self): return not self.items

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError('empty stack')
        return self.items.pop()

    def peek(self): #def peek():
        if self.is_empty():
            return None
        return self.items[-1]

    def no_items(self):
        return len(self.items)