class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
      permDiff = 0
      for i in range(len(s)):
          permDiff += abs(i - t.index(s[i]))
      return permDiff
