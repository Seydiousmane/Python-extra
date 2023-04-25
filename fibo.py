""" def fibonacci(n):
    valeur_entrer = input('Entrer un valeur positive')
    valeur = int(valeur_entrer)
    if (valeur < 2):
        return valeur
    a, b = 0,1
    for i in range(2, valeur+1):
        a, b = b, a+b
    print(b)
        

fibonacci(5) """

def fibonacci_recc(n):
    if n<2:
        return n
    else:
        return fibonacci_recc(n-1) + fibonacci_recc(n-2)
print(fibonacci_recc(4))