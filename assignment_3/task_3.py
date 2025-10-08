import sys


class Buyer:
    def __init__(self, id):
        self.id = id


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self.size = 0

    def push(self, item):
        node = Node(item)
        if self.size == 0:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self.size += 1

    def push_front(self, item):
        node = Node(item)
        if self.size == 0:
            self._head = self._tail = node
        else:
            node.next = self._head
            self._head = node
        self.size += 1

    def pop(self):
        if self._head is None:
            raise IndexError("Queue is empty")

        value = self._head.value
        self._head = self._head.next
        if self._head is None:
            self._tail = None

        self.size -= 1
        return value


class ShopQueue:
    """
    Maintain two queues: front and back.
    Keep front.size() >= back.size() and front.size() - back.size() <= 1.

    Operations:
    - regular customer: push to back, then if front.size() < back.size(), move from back to front;
    - certificate customer: if sizes equal, push to front; else push to front of back;
    - remove: pop from front, then if front.size() < back.size(), move from back to front.

    The "middle" is defined as the boundary between front and back queues:
    - even total size: middle is between the last element of front and first element of back
    - odd total size: middle is before the last element of front (which becomes the true center)
    Certificate insertion logic:
    - even queue: certificate holder becomes the new last element of front (true middle)
    - odd queue: certificate holder becomes the first element of back (inserted before the central element)

    This ensures middle insertion in O(1) while maintaining queue order.
    """

    def __init__(self):
        self._front = Queue()
        self._back = Queue()

    @property
    def size(self):
        return self._front.size + self._back.size

    def add_regular(self, buyer):
        self._back.push(buyer)
        if self._front.size < self._back.size:
            self._front.push(self._back.pop())

    def add_by_certificate(self, buyer):
        if self._front.size == self._back.size:
            self._front.push(buyer)
        else:
            self._back.push_front(buyer)

    def remove(self):
        if self._front.size == 0:
            return None
        else:
            buyer = self._front.pop()
            if self._front.size < self._back.size:
                self._front.push(self._back.pop())
            return buyer


if __name__ == "__main__":
    N = int(input())

    queues = [ShopQueue() for _ in range(N)]

    for line in sys.stdin:
        cmd = line.split()
        c_i = cmd[0]
        q_i = int(cmd[1]) if len(cmd) > 1 else None
        id_i = int(cmd[2]) if len(cmd) > 2 else None

        if c_i == "#":
            break
        else:
            if c_i == "+":
                if q_i is not None:
                    queues[q_i].add_regular(Buyer(id_i))
            elif c_i == "!":
                if q_i is not None:
                    queues[q_i].add_by_certificate(Buyer(id_i))
            elif c_i == "-":
                if q_i is not None:
                    print(queues[q_i].remove().id)
            elif c_i == "?":
                if q_i is not None:
                    print(queues[q_i].size)
