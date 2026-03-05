import random, math
nameslist = ["Juli", "Caro", "Nuria"]

def newname(index, name):
    nameslist.insert(index, name)
    print(f"eu {nameslist[i]}, querés ir a cenar?")

for i in range(len(nameslist)):
    print(f"eu, {nameslist[i]}, querés ir a cenar?")

num = random.randint(0, 2)
print(f"{nameslist[num]} no puede venir")
nameslist[num] = "Trini"
print(f"ahora viene {nameslist[num]}")
print(f"eu, {nameslist[num]}, querés ir a cenar?")

newname(0, "Ashton")
newname(math.ceil(len(nameslist)/2), "Tomi")
newname(-1, "Emi")

