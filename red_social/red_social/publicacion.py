import re
from abc import ABC, abstractmethod

LIMITE_CARACTERES = 280

class Publicacion(ABC):

    def __init__(self,autor,texto):
        self.autor = autor
        if len(texto) > LIMITE_CARACTERES or len(texto.strip()) == 0:
            raise ValueError("Texto no valido")
        self.texto = texto
        self.me_gusta = 0

    def dar_me_gusta(self):
        self.me_gusta += 1

    @property
    def hashtags(self):
        return self.extraer_hashtags(self.texto)

    @staticmethod
    def extraer_hashtags(texto):
        signos = r"[,.;:!?¡¿]"
        hashtags = [
            palabra for palabra in texto.split() 
            if palabra.startswith('#') and not re.search(signos,palabra) and palabra.islower()
        ]
        return list(dict.fromkeys(hashtags))

    @abstractmethod
    def __str__(self):
        pass

class Tweet(Publicacion):

    def __init__(self, autor, texto):
        super().__init__(autor, texto)

    def __str__(self):
        return f"{self.autor.alias}: {self.texto}"

class Respuesta(Publicacion):

    def __init__(self, autor, texto, original):
        super().__init__(autor, texto)
        self.original = original

    def __str__(self):
        return f"{self.autor.alias} ↩ {self.original.autor.alias}: {self.texto}"

class Retweet(Publicacion):

    def __init__(self, autor,original):
        super().__init__(autor,texto=original.texto)
        self.original = original
        
    def __str__(self):
        return f"{self.autor.alias} 🔁 {self.original}"
