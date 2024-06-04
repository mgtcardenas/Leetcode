class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        tmp = list(magazine)
        for character in ransomNote:
          try:
            tmp.remove(character)
          except ValueError as e:
            return False
        return True
