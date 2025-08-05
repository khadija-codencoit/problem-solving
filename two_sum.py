class Solution:
    def sum_two(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
            

nums = [2, 8, 1, 15]
target = 16
solution = Solution()
result = solution.sum_two(nums, target)
print(result)

# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# # Now, outside the class, use it like this:

# nums = [2, 8, 1, 15]
# target = 16

# solution = Solution()               # create an object of the class
# result = solution.twoSum(nums, target)  # call the function with nums and target
# print(result)      