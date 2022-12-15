from collections import deque
class Queue:
 def __init__(self):
  self._elements = deque()

 def enqueue(self, elements):
  self._elements.append(elements)

 def dequeue(self):
  return self._elements.popleft()


