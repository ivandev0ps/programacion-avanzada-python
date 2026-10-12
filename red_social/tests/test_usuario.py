import pytest 
from red_social.usuario import Usuario

def test_seguir_anade_al_otro_usuario(ana,luis):
    ana.seguir(luis)
    assert ana.sigue_a(luis) == True
    assert ana.numero_seguidos == 1
    assert luis.sigue_a(ana) == False

def test_seguirse_a_si_mismo_lanza_error(ana):
    with pytest.raises(ValueError):
        ana.seguir(ana)