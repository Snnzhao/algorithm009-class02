from collections import deque
dq=deque()
dq.append('a')
dq.append('b')
dq.append('c')
list(dq)
while len(dq)>0:
    dq.popleft()


