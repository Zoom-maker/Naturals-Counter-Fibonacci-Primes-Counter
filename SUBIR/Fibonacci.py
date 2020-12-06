#Funcion 
def Fibo(x):
    
    num = x

    def sucesion():

        if num < 2:

            return num
        
        else:

            return Fibo (num-1) + Fibo (num-2)

    return sucesion()

num = int(input("Cuantos elementos de Fibonacci desea mostrar: "))

for x in range(num):

    print(Fibo(x))