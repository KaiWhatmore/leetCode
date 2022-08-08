import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.min_heap = nums
        self.k = k
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            self.min_heap.pop(0)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            self.min_heap.pop(0)
        return self.min_heap[0]


kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))
