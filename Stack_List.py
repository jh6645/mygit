print('클래스 정의 이전 Stack')
stack=[]
def push(item):
    stack.append(item)

def peek():
    if len(stack) != 0:
        return stack[-1]

def pop():
    if len(stack)!=0:
        item=stack.pop(-1)
        return item

push('apple')
push('orange')
print(stack)    # ['apple', 'orange']
print(peek())   # orange
print(*stack)   # apple orange
print(pop())    # orange
print(stack)    # ['apple']
print(pop())    # apple
print(stack)    # []

print('\n클래스 정의 이후 Stack')
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

s=Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())
print(s.pop())
print(s.peek())