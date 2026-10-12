import pytest

from red_social.publicacion import Retweet, Tweet
from red_social.usuario import Usuario


@pytest.mark.parametrize(   
    "texto",
    [
        "",  
        " ", 
        "a"*281,
    ],
)


def test_texto_invalido_lanza_error(texto):
    fulano = Usuario("Fulano","fulano")

    with pytest.raises(ValueError):
        Tweet(fulano,texto)

@pytest.mark.parametrize(   
    "texto, esperado",
    [
        ("Hola a todos", []),
        ("Hola #Python #PYTEST",["#python", "#pytest"]),  
        ("#python y otra vez #python",["#python"] ), 
        ("Me gusta #python, y mucho #pytest!",["#python", "#pytest"] ),
    ],
)

def test_extraer_hashtags(texto,esperado):
    fulano = Usuario("Fulano","fulano")
    assert Tweet(fulano,texto).hashtags == esperado


def test_retweet_comparte_el_texto_del_original(tweet,luis):
    retweet = Retweet(luis,tweet)
    assert tweet.texto == retweet.texto
    