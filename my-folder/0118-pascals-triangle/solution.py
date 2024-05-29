class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
      result = [[1]]
      for row in range(1, numRows):
          tmp = [0]*(row + 1)  # initializing the row
          tmp[0] = 1 # first element of row
          for i in range(1, (row//2) + 1):
              tmp[i] = result[row - 1][i - 1] + result[row - 1][i]
              tmp[len(tmp) - i - 1] = result[row - 1][i - 1] + result[row - 1][i]
          tmp[-1] = 1  # last element of row
          result.append(tmp)
      return result
