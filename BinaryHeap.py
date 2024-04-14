'''
이진 힙은 우선순위큐를 구현하는 가장 기본적인 자료구조
부모의 우선순위가 자식의 우선순위보다 높은 자료구조
완전 이진 트리

스택이나 큐도 일종의 우선순위 큐이지만,
삽입되는 항목이 임의의 우선순위를 가지면
스택이나 큐는 새 항목을 삽입할 때마다
정렬 상태를 유지해야 한다는 단점이 있다.

완전 이진 트리는 1차원 배열 구현,
배열의 2번째 원소 a[1]부터 사용함.(a[0]는 사용 안 함)
'''

class BHeap:
    def __init__(self,a):
        self.a=a
        self.N=len(a)-1

    def create_heap(self):
        for i in range(self.N//2,0,-1): #leaf노드 제외하고 호출
            self.downheap(i)

    def insert(self,key):
        self.N+=1
        self.a.append(key)
        self.upheap(self.N)     #self.N은 j로 자신의 위치를 뜻함.

    def delete_min(self):       #minimum 값 삭제
        if self.N==0:
            print('Empty')
        minimum=self.a[1]
        self.a[1],self.a[-1]=self.a[-1],self.a[1]
        del self.a[-1]      #힙의 마지막 항목 삭제
        self.N-=1
        self.downheap(1)
        return minimum

    def downheap(self,i):
        while 2*i <= self.N:    #leaf노드에 도착할 때까지
            k=2*i       #k는 자신의 left child의 위치
            if k<self.N and self.a[k][0] >self.a[k+1][0]:   #left,right 비교
                k+=1    #right가 작으면 k를 right로 변경
            if self.a[i][0]<self.a[k][0]:
                break   #minheap 만족 시 break
            self.a[i],self.a[k]=self.a[k],self.a[i] #swap
            i=k

    def upheap(self,j):
        while j>1 and self.a[j//2][0]>self.a[j][0]:
            self.a[j],self.a[j//2]=self.a[j//2],self.a[j]   #swap
            j=j//2      #j는 자신의 위치를 뜻함.

    def print_heap(self):
        for i in range(1,self.N+1):
            print(' [%2d] '%self.a[i][0],self.a[i][1],']',end='')
        print(f'\n힙 크기 : {self.N}')

a=[None]
a.append([90,'watermelon'])
a.append([80,'pear'])
a.append([70,'melon'])
a.append([50,'lime'])
a.append([60,'mango'])
a.append([20,'cherry'])
a.append([30,'grape'])
b=BHeap(a)
b.print_heap()

b.create_heap()
b.print_heap()