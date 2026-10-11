import json
from collections import Counter

from red_social.usuario import Usuario


class RedSocial:

    def __init__(self):
        self.usuarios = {}
        self.publicaciones = []

    @classmethod
    def desde_json(cls,ruta):
        with open(ruta, encoding="utf-8") as f:
            datos = json.load(f)
        red_social = cls()
        for datos_usuario in datos["usuarios"]:
            usuario = Usuario.desde_dict(datos_usuario)
            red_social.usuarios[usuario.alias] = usuario #aqui se crea el usuario

        for alias, sigue_a in datos["seguimientos"]:
            usuario = red_social.usuarios[alias]
            usuario_a_seguir = red_social.usuarios[sigue_a]
            usuario.seguir(usuario_a_seguir)
        return red_social
    
    def anadir(self,usuario):
        if usuario.alias not in self.usuarios:
            self.usuarios[usuario.alias] = usuario 
        else:
            raise ValueError("El alias ya existe")
        return usuario
        
    def registrar(self,nombre, alias):
        usuario = Usuario(nombre,alias)
        return self.anadir(usuario)

    def publicar(self,publicacion):
        self.publicaciones.append(publicacion)
        return publicacion

    def tendencias(self,n=3):
        pubs_hashtags = [hash for pubs in self.publicaciones for hash in pubs.hashtags]
        return Counter(pubs_hashtags).most_common(n)
        #for hastags, veces in Counter(pubs_hashtags).most_common(n):

    def timeline(self,usuario)->list:
        lista_seguidos = usuario.seguidos
        timeline = [pub for pub in self.publicaciones if pub.autor in lista_seguidos]
        return timeline[::-1]

    def mostrar_timeline(self,alias):
        usuario = self.usuarios[alias]
        print(f"\nTimeline de {usuario.nombre} ({alias}):")
        for pub in self.timeline(usuario):
            print(pub," ♥ ",pub.me_gusta)


    def __len__(self):
        return len(self.usuarios)

    def __iter__(self):
        return iter(sorted(self.usuarios.values(), key=lambda usuario:usuario.alias))

    def __contains__(self, alias):
        return alias in self.usuarios

    def __getitem__(self, alias):
        if alias not in self.usuarios:
            raise KeyError(f"El alias {alias} no existe")
        return self.usuarios[alias]


