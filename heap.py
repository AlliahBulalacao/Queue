from heapq import heappush
from heapq import heappop
from queues import PriorityQueue


colors = []
heappush(colors, "red")
heappush(colors, "apple")
heappush(colors, "banana")

print(colors)

print(heappop(colors))
print(colors)

# another example
person1 = ("Joey", "Legend", 39)
person2 = ("Chandler", "Bing", 29)
person3 = ("Ross", "Green", 29)

print(person1 < person2)
print(person2 < person3)


CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())