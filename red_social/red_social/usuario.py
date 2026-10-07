# Terminada
class Usuario:
    def __init__(self, nombre, alias):
        self.nombre = nombre
        self.alias = "@" + alias if alias[0] != "@" else alias
        self.seguidos = []
        self._numero_seguidos = 0

    def seguir(self, otro):

        if otro in self.seguidos:
            raise ValueError(f"Ya se esta siguiendo a {otro.nombre}")

        if otro is self:
            raise ValueError("No se puede seguir a si mismo")

        self.seguidos.append(otro)
        self._numero_seguidos += 1

    @property
    def numero_seguidos(self):
        return self._numero_seguidos

    def sigue_a(self, otro):
        return otro in self.seguidos

    def a_dict(self):
        return {"nombre": self.nombre, "alias": self.alias}

    # Constructor alternativo
    @classmethod
    def desde_dict(cls, datos):
        usuario = cls(datos["nombre"], datos["alias"])
        return usuario
        # usuario.seguir_a(datos[usuario.alias])

    # Metodos especiales
    def __str__(self):
        return f"{self.nombre} ({self.alias})"

    def __eq__(self, otro):
        return self.alias == otro.alias
