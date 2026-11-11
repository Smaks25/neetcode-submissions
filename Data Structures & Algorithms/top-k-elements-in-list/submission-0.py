class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diccionario = {}

        for numero in nums:
            if numero in diccionario:
                diccionario[numero] += 1
            else:
                diccionario[numero] = 1
        return sorted(diccionario, key=diccionario.get, reverse=True)[:k]
