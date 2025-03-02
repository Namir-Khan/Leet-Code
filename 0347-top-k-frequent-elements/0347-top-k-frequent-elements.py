class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Count the number of times each element appears
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # The above count could be done using the counter lib.
        # By doing count = Counter(nums) takes T.C of 0(N)

        # Now use heap
        heap = []
        for num, freq in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            elif freq > heap[0][0]: # i.e heap's 1st element and 1st item i.e freq of the min item
                heapq.heapreplace(heap, (freq, num))

        return [num for freq, num in heap]
