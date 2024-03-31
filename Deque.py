#deque, 양방향 큐, 데크
from collections import deque
dq=deque('data')
for elem in dq:                     #이터러블 객체:for문 사용 가능한 객체?
    print(elem.upper(),end='')
print()
dq.append('r')
print(dq)
dq.appendleft('k')
print(dq)
dq.pop()
print(dq)
dq.popleft()
print(dq)
print(dq[-1])       #a
dq.extend('structure')
print(dq)
print(*dq)      #'*'은 unpacking해서 print 해 준다.
dq.extendleft('python')
print(*dq)      #중요!!!
dq.extendleft(reversed('python'))
print(*dq)

dq.clear()
print(dq)
