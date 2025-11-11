class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, priority, time, id):
        self.heap.append((-priority, time, id))
        self._sift_up(len(self.heap) - 1)
    
    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root
        
    def _sift_up(self, i):
        if i == 0:
            return
        parent = (i - 1) // 2
        if self.heap[parent] > self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self._sift_up(parent)
    
    def _sift_down(self, i):
        child1 = i * 2 + 1
        child2 = i * 2 + 2
        if child1 >= len(self.heap):
            return
        if child2 >= len(self.heap):
            child_min = child1
        else:
            child_min = child1 if self.heap[child1] < self.heap[child2] else child2
        if self.heap[child_min] < self.heap[i]:
            self.heap[i], self.heap[child_min] = self.heap[child_min], self.heap[i]
            self._sift_down(child_min)

def main():
    n = int(input())
    heap = MaxHeap()
    time_counter = 0
    
    for _ in range(n):
        data = input().split()
        if data[0] == '+':
            id = int(data[1])
            priority = int(data[2])
            heap.push(priority, time_counter, id)
            time_counter += 1
        else:
            _, _, id = heap.pop()
            print(id)

if __name__ == "__main__":
    main()
