class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_ = 1    #len_ 下划线用来解决命名冲突
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[len_] = nums[i]
                len_ += 1
        return len_

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    mm = Solution()
    result = mm. removeDuplicates(nums)
    print(result)