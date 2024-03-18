class Slist:
    class Node:
        def __init__(self,item,link):
            self.item=item
            self.link=link

    def __init__(self):
        self.head=None
        self.size=0

    def no_item(self): return self.size
    def is_empty(self): return self.size==0

    def insert_front(self,item):
        if self.is_empty:
            self.head=self.Node(item,None)
        else:
            self.head=self.Node(item,self.head)
        self.size+=1

    def insert_after(self,item,p):
        p.next=Slist.Node(item,p.next)
        self.size+=1

    def delete_front(self):
        if self.is_empty:
            raise EmptyError('underflow')
        else:
            self.head=self.head.next
            self.size-=1

    def delete_after(self,p):
        if self.is_empty:
            raise EmptyError('underflow')
        else:
            t=p.next
            p.next=t.next
            self.size-=1

    def search(self,target):
        p=self.head
        for k in range(self.size):
            if target==p.item:
                return k
            p=p.next
        return None

    def print_list(self):
        p=self.head
        while p:
            if p.link!=None:
                print(p.item,'->',end=" ")
            else:
                print(p.item)
            p=p.link

class EmptyError(Exception):
    pass

s=Slist()
s.insert_front('orange')
s.insert_front('apple')
s.insert_front('pineapple')
print(str(s.size))
s.print_list()