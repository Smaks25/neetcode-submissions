class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grupos ={}

        for palabra in strs:
            clave = "".join(sorted(palabra))
            if clave in grupos:
                grupos[clave].append(palabra)
            else:
                grupos[clave] = [palabra]
        return list(grupos.values())
    