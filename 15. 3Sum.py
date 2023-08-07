# brute force
# timed out
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        found = set()
        nums = list(sorted(nums))
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    a, b, c = nums[i], nums[j], nums[k]
                    if a + b + c == 0:
                        found.add((a, b ,c))
        return [list(each) for each in found]

# binary search for 3rd
# timed out
def bs(target, nums, s, e):
    # s and e are inclusive
    if not (0 <= s <= e <= len(nums) - 1):
        # raise ValueError(f"{target}, {nums}, {s, e}")
        return False

    while s <= e:
        guess_index = (s + e) // 2
        guess = nums[guess_index]
        if guess == target:
            return True
        elif guess < target:
            s = guess_index + 1
        elif guess > target:
            e = guess_index - 1
    return False

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # # test cases for bs
        # nums = []
        # assert not bs(0, nums, 0, 0)
        # nums = [1]
        # assert not bs(0, nums, 0, 0)
        # assert bs(1, nums, 0, 0)
        # nums = [3, 4, 5, 6]
        # assert not bs(5, nums, 0, 1)
        # assert bs(5, nums, 2, 3)


        if len(nums) < 3:
            return []
        
        found = set()
        nums = list(sorted(nums))
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])
                if bs(target, nums, j + 1, len(nums) - 1):
                    found.add((nums[i], nums[j], target))

        return [list(each) for each in found]

# Neetcode solution using pointers
# works
class Solution:
    def two_sum_2(self, target, nums, i, j):
        prev_i =  None
        while i < j:
            if nums[i] == prev_i:
                i += 1
            else:
                s = nums[i] + nums[j]
                if s > target:
                    j -= 1
                elif s < target:
                    i += 1
                else:
                    yield (nums[i], nums[j])
                    prev_i = nums[i]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = list(sorted(nums))
        prev_left = None
        left = 0
        while left + 2 < len(nums):
            if nums[left] == prev_left:
                left += 1
            else:
                target = -nums[left]
                start, stop = left + 1, len(nums) - 1
                for i, j in self.two_sum_2(target, nums, start, stop):
                    ans.append([nums[left], i, j])
                prev_left = nums[left]
        
        return ans
    
