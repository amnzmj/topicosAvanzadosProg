import random

def ruleta_rusa(camaras=6, balas=1):
    if balas >= camaras:
        return "el maximo es 6"
    
    # de que capacidad el cargador
    cilindro = ["vacía"] * camaras
    
    # random para las balas
    for _ in range(balas):
        posicion = random.randint(0, camaras - 1)
        while cilindro[posicion] == "bala":
            posicion = random.randint(0, camaras - 1)  # no 2 balas en una camara
        cilindro[posicion] = "bala"
    
    
    eleccion_jugador = random.randint(0, camaras - 1)
    
    # muerte?
    if cilindro[eleccion_jugador] == "bala":
        return "morido alv"
    else:
        return "no bala :( vivirás)"


try:
    camaras = int(input("de que tamaño es el cilindro de tu revolver? (usualmente es de 6, luego hay de 5 o de 8)") or 6)
    balas = int(input("cuantas balas vas a meter en la recamara? (que tantas ganas de desvivirte)"))
    
    resultado = ruleta_rusa(camaras, balas)
    print(resultado)
except ValueError:
    print("Por favor, ingresa números válidos.")