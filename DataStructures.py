def arrays_1():
    expenses = [2200, 2350, 2600, 2130, 2190]
    output = []

    output += [expenses[1] - expenses[0]]

    output += [expenses[0] + expenses[1] + expenses[2]]

    output += [False]
    for i in expenses:
        if i == 2000:
            output[-1] = True
            break

    expenses += [1980]

    expenses[3] -= 200

    print(expenses)
    print(output)


def arrays_2():
    heroes = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

    print(len(heroes))

    heroes += ['black panther']
    print(heroes)

    heroes.remove('black panther')
    heroes.insert(2, 'black panther')
    print(heroes)

    heroes = [heroes[0]] + ['doctor strange'] + heroes[3:]
    print(heroes)

    heroes.sort()
    print(heroes)


def arrays_3():
    max = int(input('max number: '))
    output = []
    for i in range(1, max+1, 2):
        output.append(i)
    print(output)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_at_end(self, value):
        p = self.head
        if p:
            while p.next:
                p = p.next
            p.next = Node(value)
        else:
            self.insert_at_beginning(value)

    def insert_at(self, index, value):
        if index <= 0:
            self.insert_at_beginning(value)
            return
        if index >= self.get_length():
            self.insert_at_end(value)
            return

        p = self.head
        for i in range(index-1):
            p = p.next
        node = Node(value)
        node.next = p.next
        p.next = node

    def remove_at(self, index):
        if index < 0:
            return
        if index >= self.get_length():
            return
        dummy = Node("dummy")
        dummy.next = self.head
        p = dummy
        for i in range(index):
            p = p.next
        p.next = p.next.next
        self.head = dummy.next

        # if index == 0:
        #     self.head = self.head.next
        #     return
        #
        # p = self.head
        #
        # for i in range(index-1):
        #     p = p.next
        # p.next = p.next.next

    def print(self):
        p = self.head
        while p:
            print(p.value, end=" -> ")
            p = p.next

    def get_length(self):
        length = 0
        p = self.head
        while p:
            length += 1
            p = p.next
        return length


link = LinkedList()
for i in range(10):
    link.insert_at_end(i)
# link.insert_at_beginning(1)
link.remove_at(-1)
link.print()