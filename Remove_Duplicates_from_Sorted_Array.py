#Remove Duplicates from Sorted Array, Array
class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    k = 0

    for newArray in nums:
      if k < 1 or newArray > nums[k - 1]:
        nums[k] = newArray
        k += 1

    return k
