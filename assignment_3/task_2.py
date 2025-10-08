class NoSuchCommandException(Exception):
    def __init__(self, command: str):
        super().__init__(f"No such command exception `{command}`")


class Deque:
    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self.elements = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    @property
    def len(self):
        return self.size

    def push_back(self, item):
        if self.len == self.capacity:
            return False
        self.elements[self.tail] = item
        self.tail = self.__calculate_index(self.tail + 1)
        self.size += 1
        return True

    def push_front(self, item):
        if self.len == self.capacity:
            return False
        self.head = self.__calculate_index(self.head - 1)
        self.elements[self.head] = item
        self.size += 1
        return True

    def pop_back(self):
        if self.len == 0:
            return None
        self.tail = self.__calculate_index(self.tail - 1)
        item = self.elements[self.tail]
        self.elements[self.tail] = None
        self.size -= 1
        return item

    def pop_front(self):
        if self.len == 0:
            return None
        item = self.elements[self.head]
        self.elements[self.head] = None
        self.head = self.__calculate_index(self.head + 1)
        self.size -= 1
        return item

    def __calculate_index(self, item):
        if item > self.capacity - 1:
            return item % self.capacity
        if item < 0:
            return (item + self.capacity) % self.capacity
        return item


PUSH_BACK = "0"
PUSH_FRONT = "1"
LEN = "2"
POP_BACK = "3"
POP_FRONT = "4"
EOI = "-1"
ERROR = "Error!"


def process_command(deque, command, result):
    if command[0] == PUSH_BACK:
        if not deque.push_back(int(command[1])):
            result.append(ERROR)
    elif command[0] == PUSH_FRONT:
        if not deque.push_front(int(command[1])):
            result.append(ERROR)
    elif command[0] == POP_BACK:
        item = deque.pop_back()
        result.append(str(item) if item is not None else ERROR)
    elif command[0] == POP_FRONT:
        item = deque.pop_front()
        result.append(str(item) if item is not None else ERROR)
    elif command[0] == LEN:
        result.append(str(deque.len))
    else:
        raise NoSuchCommandException(command[0])


if __name__ == "__main__":
    deque = Deque(100000)
    result = []
    while True:
        source = input().split()
        request = (source[0], int(source[1]) if len(source) > 1 else None)
        if request[0] == EOI:
            break
        process_command(deque, request, result)
    print("\n".join(result))
