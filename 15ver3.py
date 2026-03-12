glosario = {"cast" : "pasar una variable de un tipo de dato a otro", 
            "iterable" : "cualquier dato sobre el que se pueda recorrer parte por parte definida", 
            "hard code" : "hacer un programa inflexible, inutilizable para ser reusado",
            ".items()" : "método para diccionarios que devuelve una tupla por cada set clave:valor",
            "#!/usr/bin/bash" : "línea que se debería escribir sobre cada script de bash para que se use el lenguaje (en este caso, formateado para linux)",
            ".lower()" : "método para strings que las hace todas minúsculas",
            ".upper()" : "método para strings que las hace todas mayúsculas",
            ".values()" : "método para diccionarios que devuelve sus valores"}

for i in glosario.items():
    print(f"{i[0]} : \n {i[1]}")
