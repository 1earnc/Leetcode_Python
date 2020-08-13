"""
The two pointers i and n start at the same time and point to a position. When the current value does not need to be larger
than the previous one, it means that 3 are present.Or more than 3 identical values, at this time the if condition is not satisfied,
i stays in the unsatisfied position, waiting for the next larger number to be replaced, when the next larger one appears
The number again satisfies the if condition, replacing the position pointed to by i with the number,
i pointing to the next waiting for replacement, and the if condition is again used to detect the replacement.
The number is guaranteed to not appear more than two repetitions.
"""


class Solution:
    def removeDuplicates(self, nums):
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    mm = Solution()
    result = mm.removeDuplicates(nums)
    print(result)
