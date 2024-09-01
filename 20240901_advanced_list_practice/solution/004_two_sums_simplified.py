"""
Assume nums is sorted ascending already
"""
nums: list[int] = [2,7,11,15]
target = 9

"""
Find the index where the two numbers add up to 9

[0, 1]
"""

left_index: int = 0   # start from left
right_index: int = len(nums) - 1    # start from right

while nums[left_index] + nums[right_index] != target:
    if nums[left_index] + nums[right_index] < target:
        left_index += 1
    else:
        right_index -= 1

print([left_index, right_index])