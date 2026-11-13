from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(palabra)}:{palabra}" for palabra in strs)

    def decode(self, s: str) -> List[str]:
        resultado = []
        posicion_actual = 0 
        
        while posicion_actual < len(s):
            # Buscamos los dos puntos a partir de la posición actual
            posicion_dos_puntos = s.find(":", posicion_actual)
            
            # Extraemos el tamaño de la palabra
            largo_palabra = int(s[posicion_actual : posicion_dos_puntos])
            
            # Añadimos la palabra usando el tamaño exacto al resultado
            inicio_palabra = posicion_dos_puntos + 1
            fin_palabra = inicio_palabra + largo_palabra
            resultado.append(s[inicio_palabra : fin_palabra])
            
            # Movemos el cursor al final de la palabra actual
            posicion_actual = fin_palabra
            
        return resultado