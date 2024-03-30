class Node:
    def __init__(self,item,link):
        self.item=item
        self.next=link

def push(item):
    global top
    global size
    top=Node(item,top)
    size+=1

def peek():
    if size!=0:
        return top.item

def pop():
    global top
    global size
    if size!=0:
        top_item=top.item
        top=top.next
        size-=1
        return top_item

def print_stack():
    print('\ttop ->\t',end='')
    p=top
    print('\t',p.item)
    p=p.next
    while p:
        if p.next!=None:
            print('\t\t\t\t',p.item)
        else:
            print('\t\t\t\t',p.item)
        p=p.next
    print()

top=None    #초기화
size=0      #초기화
push('apple')
push('orange')
push('cherry')
print('사과, 오렌지, 체리 push 후:\n',end='')
print_stack()
print('top 항목: ',end='')
print(peek())
push('pear')
print('배 push 후:\t\t')
print_stack()
pop()
push('grape')
print('pop(), 포도 push 후:\t')
print_stack()