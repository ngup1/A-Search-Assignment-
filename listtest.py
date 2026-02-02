from list import *

# Usage: python "list test.py"

if __name__ == '__main__':


    # Queue

    queue = Queue()

    queue.add('A')
    queue.add('B')
    queue.add('C')
    queue.add('D')
    queue.add('E')

    print ("\nQueue ", queue, "\n")

    while not queue.empty():
        x = queue.remove()

        print (x)

    queue = Queue()

    queue.add(Node('1', None))
    queue.add(Node('2', '1', 5, 5))
    queue.add(Node('3', '1', 1, 2))

    print ("\nQueue ", queue, "\n")

    while not queue.empty():
        x = queue.remove()

        print (x)


    # Stack

    stack = Stack()

    stack.add('A')
    stack.add('B')
    stack.add('C')
    stack.add('D')
    stack.add('E')

    print ("\nStack ", stack, "\n")

    while not stack.empty():
        x = stack.remove()

        print (x)

    stack = Stack()

    stack.add(Node('1', None))
    stack.add(Node('2', '1', 5, 5))
    stack.add(Node('3', '1', 1, 2))

    print ("\nStack ", stack, "\n")

    while not stack.empty():
        x = stack.remove()

        print (x)


    # Priority queue

    priority_queue = PriorityQueue()

    priority_queue.add(Node('S', None, 0, 6))
    priority_queue.add(Node('A', 'S', 1, 3))
    priority_queue.add(Node('B', 'S', 1, 5))
    priority_queue.add(Node('C', 'A', 1, 2))
    priority_queue.add(Node('D', 'A', 1, 4))
    priority_queue.add(Node('E', 'B', 1, 1))

    print ("\nPriority Queue ", priority_queue, "\n")

    while not priority_queue.empty():
        x = priority_queue.remove()

        print (x) 