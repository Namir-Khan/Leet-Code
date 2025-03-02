class NumArray:

    def __init__(self, nums: List[int]):
        self.add_nums = [0]
        for num in nums:
            self.add_nums.append(self.add_nums[-1] + num)


    def sumRange(self, left: int, right: int) -> int:
        return self.add_nums[right+1] - self.add_nums[left] # Here we use a dp approach with prefix sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)