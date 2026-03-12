from city_functions import ciudadpais

def test_ciudad_pais():
    string = ciudadpais("Buenos Aires", "Argentina")
    assert string == "Buenos Aires, Argentina"
