# heaps.py


class Heap:
    def __init__(self) -> None:
        self._items = []

    def add(self, value):
        self._items.append(value)

    def parent_index(self, index: int) -> int:
        return int((index - 1) / 2)

    def left_child_index(self, index: int) -> int:
        return index * 2 + 1

    def right_child_index(self, index: int) -> int:
        return index * 2 + 2

    def parent(self, index: int):
        return self._items[self.parent_index(index)]

    def left_child(self, index: int):
        return self._items[self.left_child_index(index)]

    def right_child(self, index: int):
        return self._items[self.right_child_index(index)]

    def has_parent(self, index) -> bool:
        return self.parent_index(index) >= 0

    def has_left_child(self, index) -> bool:
        return self.left_child_index(index) < len(self._items)

    def has_right_child(self, index) -> bool:
        return self.right_child_index(index) < len(self._items)

    def print(self):
        for i, _ in enumerate(self._items):
            lc = None
            rc = None
            if self.has_left_child(i):
                lc = self._items[self.left_child_index(i)]
            if self.has_right_child(i):
                rc = self._items[self.right_child_index(i)]
            print(f"{self._items[i]} => {lc}, {rc}")

    def peak(self):
        if len(self._items) == 0:
            raise ValueError("Heap is empty")


class MinHeap(Heap):
    def __init__(self, size=10) -> None:
        super().__init__()

    def _swap(self, index1, index2) -> None:
        tmp = self._items[index1]
        self._items[index1] = self._items[index2]
        self._items[index2] = tmp

    def poll(self):
        """Remove minimum element"""
        if len(self._items) == 0:
            raise ValueError("Heap is empty")
        # Grab first
        item = self._items[0]
        # Move last to first
        self._items[0] = self._items[-1]
        self._items = self._items[:-1]
        self.heapify_down()
        return item

    def add(self, value):
        super().add(value)
        self.heapify_up()

    def heapify_up(self):
        # Start with last element
        index = len(self._items) - 1
        print(self._items)

        while self.has_parent(index) and self.parent(index) > self._items[index]:
            self._swap(self.parent_index(index), index)
            index = self.parent_index(index)
            print(self._items)

    def heapify_down(self):
        # Start with first element
        index = 0
        while self.has_left_child(index):
            min_child_index = self.left_child_index(index)

            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                min_child_index = self.right_child_index(index)

            if self._items[index] < self._items[min_child_index]:
                break
            else:
                self._swap(index, min_child_index)

            index = min_child_index



# heap = Heap()

# heap.add('A')
# heap.add('B')
# heap.add('C')
# heap.add('D')
# heap.add('E')
# heap.add('F')
# heap.add('G')
# heap.print()

min_heap = MinHeap()
min_heap.add(10)
min_heap.add(15)
min_heap.add(20)
min_heap.add(17)
print(min_heap._items)

min_heap.add(8)
print(min_heap._items)

print("poll")
min_heap.poll()
print(min_heap._items)
