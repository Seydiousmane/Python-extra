import time
DUREE_PROGRESSION = 10
print('Ce programme vous propose 3 options pour votre cuisson')
print('1 - Temps de cuisson pour les oeufs à la coque : 3 minutes')
print('2 - Temps de cuisson pour les oeufs mollets : 6 minutes')
print('1 - Temps de cuisson pour les oeufs durs : 9 minutes')
choix = input("Que voulez-vous cuire ?")

duree = 0
if choix == "1":
    duree = 12
elif choix == "2":
    duree = 6 * 60
elif choix == "3":
    duree = 9 * 60

while True:
    for i in range(0, DUREE_PROGRESSION):
        time.sleep(1)
        duree-=1
        print('.', end="", flush=True)
        if duree <=0:
            break
    if duree <=0:
        break
    min=duree//60
    sec=duree-min*60
    print()
    print(f"Temps restant {min:02d}:{sec:02d} ")

