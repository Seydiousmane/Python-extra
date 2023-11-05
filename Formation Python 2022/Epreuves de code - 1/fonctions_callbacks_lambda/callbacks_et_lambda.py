def add_callback(a, b):
    return a+b


def mult_callback(a, b):
    return a*b


def afficher_table(n, operateur, operation_cbk):
    for i in range(1, 10):
        print(i, operateur, n, "=", operation_cbk(i, n))


afficher_table(2, "+", lambda a, b : a + b)
