class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for posicion in range(len(nums)):
            for contar in range(posicion + 1, len(nums)):
                    if nums[posicion] + nums[contar] == target:
                        return [posicion, contar]

        return []