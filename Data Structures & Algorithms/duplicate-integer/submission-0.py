class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vistos = set()
        for numero in nums:
            if numero in vistos:
                return True
            else:
                vistos.add(numero) 
        return False
