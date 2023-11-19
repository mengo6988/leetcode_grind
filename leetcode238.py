def productExceptSelf(self, nums: List[int]) -> List[int]:
	n = len(nums)
	res = [1] * n
	for i in range(n):
		for l in range(i):
			res[i] *= nums[l]
			l += 1
		for r in range (i+1, n):
			res[i] *= nums[r]
			r += 1
		i += 1
	return res
# Time: O(n^2)
# Space: O(n)
# Brute Force
# Loops through the left and right side of the array and multiplies the values

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        resr = [1] * n
        for i in range(1, n):
            res[i] = nums[i - 1] * res[i - 1]
        for i in range(n-2, -1, -1):
            resr[i] = nums[i + 1] * resr[i + 1]
        for i in range(n):
            res[i] *= resr[i]
        return res
# Time: O(n)
# Space: O(n)
# Dynamic Programming

def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            res[i] = nums[i - 1] * res[i - 1]
        right = 1
        for i in range(n-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res

