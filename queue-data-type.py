from queues import Queue

fifo = Queue()
fifo.enqueue("9th")
fifo.enqueue("8th")
fifo.enqueue("7th")

fifo.dequeue()
'9th'
fifo.dequeue()
'8th'
fifo.dequeue()
'7th'

from queues import Queue

fifo = Queue("9th", "8th", "7th")
len(fifo)

for element in fifo:
     print(element)

len(fifo)

