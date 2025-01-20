import random

def adivina_el_numero():
    print("¡Bienvenido al juego de Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 10.")
    print("Trata de adivinarlo.")
    
    # Genera un número aleatorio entre 1 y 10
    numero_secreto = random.randint(1, 10)
    
    while True:
        try:
            # Pide al usuario que adivine el número
            adivinanza = int(input("Escribe tu número: "))
            
            if adivinanza < 1 or adivinanza > 10:
                print("Por favor, elige un número entre 1 y 10.")
            elif adivinanza < numero_secreto:
                print("El número es más alto.")
            elif adivinanza > numero_secreto:
                print("El número es más bajo.")
            else:
                print(f"¡Felicidades! Adivinaste el número: {numero_secreto}")
                break
        except ValueError:
            print("Por favor, escribe un número válido.")

# Ejecuta el juego
adivina_el_numero()