platformes_sociales = (["Facebook", "Instagram", True, "Twitter"],[True,False,False,True])
print(platformes_sociales)
print(platformes_sociales,len(platformes_sociales))
platformes_sociales[0].insert(2,"Snapchat")
print(platformes_sociales,len(platformes_sociales))
print(platformes_sociales[0].pop(3))
print(platformes_sociales,len(platformes_sociales))
print(True in platformes_sociales[0])

# Exercice
fruits = ["pomme", "banane", "orange"]
print(fruits)
fruits.append("kiwi")
print(fruits)
fruits.remove("orange")
print(fruits)
fruits[1] = "ananas"
print(fruits)
print(len(fruits))
fruits.sort()
print(fruits)