class CList:
    class Node:
        def __init__(self,item,link):
            self.item=item
            self.next=link  #next가 인스턴스 변수!
    def  __init__(self):
        self.last=None
        self.size=0

    def no_items(self): return self.size
    def is_empty(self): return self.size==0

    def insert(self,item):
        n=self.Node(item,None)  #새 노드 생성하여 n이 참조
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
        self.size+=1

    def first(self):
        if self.is_empty():
            raise EmptyError('No Items')
        f=self.last.next
        return f.item

    def delete(self):
        if self.is_empty():
            raise EmptyError('No Items')
        x=self.last.next
        if self.size==1:
            self.last=None
        else:
            self.last.next=x.next
        self.size-=1
        return x.item

    def print_list(self):
        if self.is_empty():
            print('List is empty Now')
        else:
            f=self.last.next
            p=f
            while p.next!=f:
                print(p.item,' -> ',end=' ')
                p=p.next
            print(p.item)

class EmptyError(Exception):
    pass