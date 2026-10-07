from abc import ABC, abstractmethod
import re
LIMITE_CARACTERES = 280

class Publicacion:

    def __init__(self,autor,texto):
        self.autor = autor
        if len(texto) == 0 or len(texto) > 280 or len(texto.strip()) == 0:
            raise ValueError("Texto no valido")
        self.texto = texto
        self.me_gusta = 0

    def dar_me_gusta(self):
        return self.me_gusta + 1

    @property
    def hashtags(self):
        return self.extraer_hastags(self.texto)

    @staticmethod
    def extraer_hastags(texto):
        signos = r",.;:!?¡¿"
        hashtags = [
            palabra for palabra in texto.split() 
            if palabra.startswith('#') and not re.search(signos,palabra) and palabra.islower()
        ]
        return list(dict.fromkeys(hashtags))

    @abstractmethod
    def __str__(self):
        pass