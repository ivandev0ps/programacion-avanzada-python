import json
from red_social.red import RedSocial
from red_social.publicacion import Tweet

def test_timeline_solo_tiene_publicaciones_de_los_seguidos(red):
    red.publicar(Tweet(red["@ana"],"Hola a todos #python #pytest"))
    assert len(red.timeline(red["@luis"])) == 1
    assert red.timeline(red["@ana"]) == []

def test_desde_json_construye_usuarios_y_seguimientos(mocker):

    datos = {
        "usuarios": [
            {"nombre": "Ana", "alias": "@ana"},
            {"nombre": "Luis", "alias": "@luis"},
            {"nombre": "Marta", "alias": "@marta"}
        ],
        "seguimientos": [
            ["@luis", "@ana"],
            ["@marta", "@ana"],
            ["@marta", "@luis"]
        ]
    }

    mock_open = mocker.mock_open(read_data=json.dumps(datos))
    mocker.patch("builtins.open", mock_open)

    red = RedSocial.desde_json("")

    mock_open.assert_called_once_with("", encoding="utf-8")

    assert len(red.usuarios) == 3
    assert red["@luis"].sigue_a(red["@ana"])
    assert red["@marta"].sigue_a(red["@ana"])
    assert red["@marta"].sigue_a(red["@luis"])
    assert not red["@ana"].sigue_a(red["@luis"])
    assert not red["@ana"].sigue_a(red["@marta"])
    assert not red["@luis"].sigue_a(red["@marta"])