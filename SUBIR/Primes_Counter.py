def primos(x):
    
    limite = x + 1

    def next():

        cont = 0

        for x in range(1, limite):

            for y in range(1, x + 1):

                if x % y == 0:
                    cont += 1

            if cont == 2:
                print(x)

            cont = 0

    next()    

num = int(input("Ingrese hasta que numero desea mostrar los numeros primos: "))

primos(num)
