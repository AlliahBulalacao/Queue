from queues import Stack

lifo = Stack("9th", "8th", "7th")
for element in lifo:
    print(element)

lifo = []

lifo.append("9th")
lifo.append("8th")
lifo.append("7th")

lifo.pop()
'9th'
lifo.pop()
'8th'
lifo.pop()
'7th'


