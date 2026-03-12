juli =  {"nombre" : "Julián", "edad" : 23, "ciudad" : "Avellaneda"}
caro = {"nombre" : "Carolina", "edad" : 31, "ciudad" : "Gerli"}
carmen = {"nombre" : "Carmen", "edad" : 79, "ciudad" : "Gerli"}
gente = [juli, caro, carmen]
for i in gente:
    print(f"Nombre:{i['nombre']}\nEdad:{i['edad']}\nCiudad:{i['ciudad']}")
