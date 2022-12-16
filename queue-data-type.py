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

fifo = Queue()
fifo.enqueue("red")
fifo.enqueue("yellow")
fifo.enqueue("blue")

fifo.dequeue()
fifo.dequeue()
fifo.dequeue()

fifo = Queue("red", "yellow", "blue")
len(fifo)

for element in fifo:
     print(element)




