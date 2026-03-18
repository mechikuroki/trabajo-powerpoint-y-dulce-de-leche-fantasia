from city_functions import ciudadpais

def test_ciudad_pais_pasa():
    string = ciudadpais("Buenos Aires", "Argentina")
    assert string == "Buenos Aires, Argentina"

def test_ciudad_pais_falla():
    string = ciudadpais("Gerli", "Buenos Aires", "Argentina")
    assert string == "Gerli, Buenos Aires, Argentina"


