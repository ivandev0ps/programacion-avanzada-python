from red_social.publicacion import Respuesta, Retweet, Tweet
from red_social.red import RedSocial


def main():
    # 1. La red se carga desde un fichero: usuarios y quién sigue a quién
    red = RedSocial.desde_json("datos/usuarios.json")
    print(f"Usuarios registrados: {len(red)}")
    for usuario in red:
        print(f"  {usuario} sigue a {usuario.numero_seguidos}")

    # 2. Un usuario nuevo que empieza a seguir a otro
    pablo = red.registrar("Pablo", "pablo")
    print(f"\nNuevo usuario: {pablo}")
    print(f"¿Está @pablo en la red? {'@pablo' in red}")
    pablo.seguir(red["@ana"])
    print(f"¿Sigue @pablo a @ana? {pablo.sigue_a(red['@ana'])}")
    print(f"¿Sigue @ana a @pablo? {red['@ana'].sigue_a(pablo)}")


    # 3. Publicaciones de tres tipos distintos
    ana, luis, marta = red["@ana"], red["@luis"], red["@marta"]
    hola = red.publicar(Tweet(ana, "Hola a todos #python #pytest"))
    red.publicar(Respuesta(luis, "¡Bienvenida! #Python", hola))
    red.publicar(Retweet(marta, hola))
    red.publicar(Tweet(pablo, "Mi primer tweet #hola"))

    # 4. Me gusta, y cada publicación se muestra a su manera
    hola.dar_me_gusta()
    hola.dar_me_gusta()
    print("\nPublicaciones:")
    for publicacion in red.publicaciones:
        print(f"  {publicacion}  ♥ {publicacion.me_gusta}")
    print(f"\nHashtags del tweet de {ana}: {hola.hashtags}")

    # 5. Timeline y tendencias
    red.mostrar_timeline("@marta")
    print("\nTendencias:")
    for hashtag, veces in red.tendencias(2):
        print(f"  {hashtag} ({veces})")

if __name__ == "__main__":
    main()

"""
from red_social.publicacion import Respuesta, Retweet, Tweet
from red_social.usuario import Usuario


def main():

    pepe = Usuario("Pepe", "pepe")
    manolo = Usuario("Manolo", "@manolo")
    venancio = Usuario("Venancio", "venancio")

    print(pepe.alias)

    pepe.seguir(manolo)
    pepe.seguir(venancio)
   
    print("#seguidos de Pepe",pepe.numero_seguidos)

    print(pepe)
    print(manolo)

    print(pepe == manolo)

    print("--------")
    for seguido in pepe.seguidos:
        print(seguido.alias)
    print("--------")



    tw1 = Tweet(pepe, "Hola a todos #ostia #chavales")
    print(f"Tweet de {pepe.nombre}: ",tw1)

    resp1 = Respuesta(venancio, "Bienvenido #chaval",tw1)
    print(f"Respuesta de {venancio.nombre}",resp1)

    retw1 = Retweet(manolo, tw1)
    print(f"Retweet de {manolo.nombre} de un tweet ", retw1)
    retw2 = Retweet(manolo, resp1)
    print(f"Retweet de {manolo.nombre} de una respuesta: ", retw2)

    print("--------")
    print(retw2.autor.nombre)
    #print(tw1.texto)
    print("--------")

    print("hastags de la tw1: ", tw1.hashtags)

    publicaciones = [tw1,resp1,retw1,retw2]

    publicaciones = [pubs for pubs in publicaciones]
    for pubs in publicaciones:
        if pubs.autor.alias == '@pepe':
            print(pubs.autor)


if __name__ == "__main__":
    main()
"""

