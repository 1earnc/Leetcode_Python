class Solution:
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:

            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if nums[start] <= target and target < nums[mid]:
                    if target == nums[start]: return start
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[end] >= target and target > nums[mid]:
                    if target == nums[end]: return end
                    start = mid + 1
                else:
                    end = mid - 1

        return -1

if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 0
    mm = Solution()
    result = mm. search(nums, target)
    print(result)
