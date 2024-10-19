#Reverse string, string. Write a function that reverses a string. The input string is given as an array of characters s. Python3
class Solution:
  def reverseString(self, s: List[str]) -> None:
    l = 0
    r = len(s) - 1

    while l < r:
      s[l], s[r] = s[r], s[l]
      l += 1
      r -= 1
