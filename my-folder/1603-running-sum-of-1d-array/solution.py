class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
      result = []
      tmp = 0
      for num in nums:
        result.append(tmp + num)
        tmp += num
      return result
