from src.main import resultado_ronda

def test_empate():
    assert resultado_ronda("piedra", "piedra") == "empate"

def test_gana_usuario():
    assert resultado_ronda("papel", "piedra") == "gana_usuario"

def test_gana_pc():
    assert resultado_ronda("tijera", "piedra") == "gana_pc"
