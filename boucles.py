from operator import truediv


jeu_lance = True
print("")

while jeu_lance:
    option = input(">")
    if option == "again":
        continue
    elif option == "quit":
        jeu_lance = False
    elif option == 'hello':
        print('Hello')
print("A plus")