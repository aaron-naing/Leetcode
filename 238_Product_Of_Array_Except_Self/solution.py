"""
Problem Statement:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""



class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [1 for _ in range(len(nums))]
        pre = 1
        post = 1

        for i in range(len(nums)):
            ans[i] *= pre # left half
            pre *= nums[i] # update pre

            j = len(nums) - i - 1 
            ans[j] *= post # right half
            post *= nums[j] # update post
        return ans



if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1,2,3,4]))




