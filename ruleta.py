import random

def ruleta_rusa(camaras=6, balas=1):
    if balas >= camaras:
        return "el maximo es 6"
    
    # Creamos una lista que representa las cámaras del revólver
    cilindro = ["vacía"] * camaras
    
    # Colocamos las balas en posiciones aleatorias
    for _ in range(balas):
        posicion = random.randint(0, camaras - 1)
        while cilindro[posicion] == "bala":
            posicion = random.randint(0, camaras - 1)  # Evitamos colocar dos balas en la misma cámara
        cilindro[posicion] = "bala"
    
    # El jugador elige una cámara al azar
    eleccion_jugador = random.randint(0, camaras - 1)
    
    # Comprobamos el resultado
    if cilindro[eleccion_jugador] == "bala":
        return "morido alv"
    else:
        return "no bala :( vivirás)"

# Interacción con el usuario
try:
    camaras = int(input("de que tamaño es el cilindro de tu revolver? (usualmente es de 6, luego hay de 5 o de 8)") or 6)
    balas = int(input("cuantas balas vas a meter en la recamara? (que tantas ganas de desvivirte)"))
    
    resultado = ruleta_rusa(camaras, balas)
    print(resultado)
except ValueError:
    print("Por favor, ingresa números válidos.")