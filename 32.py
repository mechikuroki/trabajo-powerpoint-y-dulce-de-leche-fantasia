from pathlib import Path
path = Path("pi.txt")
print(path)
cumple = input("Ingresa tu cumpleaños, en la forma ddmmaa:")
with open(path, "r") as f:
    pi = f.read()
    if cumple in pi:
        print("Tu cumple está en el primer millón de dígitos de pi!!!")
    else:
        print("Tu cumple no está en el primer millón de dígitos de pi :(")

