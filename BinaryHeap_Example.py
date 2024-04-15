import heapq
hp=[]
heapq.heappush(hp,4)    #insert와 동일
heapq.heappush(hp,8)
heapq.heappush(hp,1)
heapq.heappush(hp,6)
print(hp)
print(heapq.heappop(hp),end=' ')    #deletemin과 동일
print(heapq.heappop(hp),end=' ')
print(heapq.heappop(hp),end=' ')
print(heapq.heappop(hp))

a=[3,5,1,2,6,8,7]
print(a)
heapq.heapify(a)    #createheap과 동일
print(a)