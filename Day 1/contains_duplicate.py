class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set =set()   # Making the set of numbers
        for i in nums:
            if i in num_set:   #if the number is already present in the set then return true
                return True
            else:
                num_set.add(i)   # else add the number, the iteration will go on.
        return False  # none found, return False
        