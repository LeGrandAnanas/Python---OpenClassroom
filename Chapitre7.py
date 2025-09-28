# nouvelle_campagne = {
# "responsable_de_campagne": "Jeanne d'Arc",
# "nom_de_campagne": "Campagne nous aimons les chiens",
# "date_de_début": "01/01/2020",
# "influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
# }
# print(nouvelle_campagne)
# print(nouvelle_campagne["responsable_de_campagne"])

# taux_de_conversion = {}
# taux_de_conversion['facebook'] = 3.4
# taux_de_conversion['instagram'] = 1.2
# print(taux_de_conversion)
# taux_de_conversion = dict()
# taux_de_conversion['facebook'] = 3.4
# taux_de_conversion['instagram'] = 1.2
# print(taux_de_conversion)

#Excercice
fruits = {"pomme":"rouge", "banane":"jaune", "orange":"orange"}
fruits["kiwi"] = "vert"
couleur_banane = fruits["banane"]
fruits["pomme"]="vert"
fruits.pop("banane")
print(fruits.keys())