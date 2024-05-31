class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
      answer = []
      for i in range(1, n + 1):
          match i:
              case i if i % 3 == 0 and i % 5 == 0:
                  answer.append("FizzBuzz")
              case i if i % 3 == 0:
                  answer.append("Fizz")
              case i if i % 5 == 0:
                  answer.append("Buzz")
              case _:
                  answer.append(str(i))
      return answer
