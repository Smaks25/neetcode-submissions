class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        conteo = {}
        for caracter in s:
            conteo[caracter] = conteo.get(caracter, 0) + 1
        for caracter in t:
            if caracter not in conteo or conteo[caracter] == 0:
                return False
            conteo[caracter]-=1
        return True