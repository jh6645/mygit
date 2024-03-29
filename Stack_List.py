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