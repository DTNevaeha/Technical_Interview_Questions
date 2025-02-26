# Two Sums
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''


def targetElements(numberList, targetNumber):
    for number in numberList:
        for element in numberList:
            if number + element == targetNumber and numberList.index(number) != numberList.index(element):
                return [numberList.index(number), numberList.index(element)]
    return []


print("TargetElements")
print(targetElements([5, 4, 2, 3], 5)) # Output: [2,3]
print(targetElements([2, 4, -3, 8], 1)) # Output: [1,2]
print(targetElements([1, 2, 3, 4], 8)) # Output: []


class Solution(object):
    def twoSum(self, nums, target) -> list[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {} # Dictionary to store the number and its index
        for element, num in enumerate(nums): # Loop over the nums[]. Enumerate provides both indext and value of each element.
            value = target - num
            if value in num_dict: # Checks to see if the value is already in the dictionary
                return [num_dict[value], element] # If the value is in the dictionary, return the index of the value and the current index
            num_dict[num] = element # If the value is not in the dictionary, add the number and its index to the dictionary
        return [] # If no solution is found, return an empty list


nums: list[int] = [2,7,11,15]
target: int = 9
solution = Solution()
print()
print("twoSum")
print(solution.twoSum(nums, target)) # Output: [0,1]
print(solution.twoSum([3,2,4], 6)) # Output: [1,2]
print(solution.twoSum([3,3], 6)) # Output: [0,1]
print(solution.twoSum([0,3,5,15,8], 9)) # Output: []

