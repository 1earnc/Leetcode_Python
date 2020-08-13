class Solution:
    #O(n) + O(n) = O(n)
    def twoSum(self, nums, target):
        index = {}
        #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
        for i, num in enumerate(nums):
            if target - num in index:
                return [index[target-num], i]
            else:
                index[num] = i

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    mm = Solution()  # TODO 1.创建对象时，只需使用类名，且类名后面要带括号！
    result = mm.twoSum(nums, target)  # TODO 2.然后使用创建的对象调用该类的方法，并把调用该方法得到的结果赋值给变量result
    print(result)

