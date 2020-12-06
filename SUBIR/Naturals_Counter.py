#Funcion 
def counter(x) :

    limite = x + 1

    def inside() :
        
        for f in range(0, limite):
             print(f)
            
    inside()

num = int(input("Ingrese el numero hasta el que desea mostrar: "))

counter(num)