lenguajes_favoritos = {'Juan': 'python', 'Sara': 'c', 'Eduardo': 'rust', 'Agustina': 'c#'}
gente = ["Juan", "Caro", "Juli", "Eduardo", "Evaristo"]
for i in gente:
    if i in lenguajes_favoritos.keys():
        print("Gracias por contestar :)")
    else:
        print("Contesta esta encuesta?")
