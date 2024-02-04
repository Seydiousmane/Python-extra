pizzas_noms = ("4 fromages", "Calzone", "Hawai")
pizzas_prix = (10.5, 11, 25)

pizzas_noms_et_prix = zip(pizzas_noms, pizzas_prix) 
print(pizzas_noms_et_prix)#<zip object at 0x0000020CAE73EE40>

#Pour parcourir les données du zip on peut utliser list
pizzas_noms_et_prix = list(zip(pizzas_noms, pizzas_prix)) 
for (nom, prix) in pizzas_noms_et_prix:
    print(f"{nom} - {prix}")


for (nom, prix) in zip(pizzas_noms, pizzas_prix):
    print(f"{nom} - {prix}")


#Unzipped un zip
unzipped = list(zip(*pizzas_noms_et_prix)) #* permet d'eclater pizzas_noms_et_prix

pn, pp = list( zip(*pizzas_noms_et_prix)) 