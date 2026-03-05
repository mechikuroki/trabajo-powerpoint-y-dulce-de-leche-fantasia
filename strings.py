mystring = input("string: ")
#el método center pone en el medio la string sobre la que se hace el mísmo
#en una string de la cantidad de caracteres aportados en el primer parámetro,
#rodeado del segundo
centeredstring = mystring.center(40, "-")
print("centered string:", centeredstring)
#el método casefold pasa todos los caracteres a minúscula y sin
#caracteres que "sobrepasen" a los otros
casefoldstring = mystring.casefold()
print("casefold string:", casefoldstring)
