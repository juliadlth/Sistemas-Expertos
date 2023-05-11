 import random

# Definimos las posibles opciones para el juego
personajes = ['Scarlett', 'Mustard', 'Peacock', 'Green', 'Plum']
locaciones = ['Cocina', 'Salón', 'Biblioteca', 'Estudio', 'Comedor']
armas = ['Candelabro', 'Cuchillo', 'Pistola', 'Soga', 'Tubería']

# Definimos 5 historias posibles del asesinato
historias = [
    {
        'asesino': 'Scarlett',
        'locacion': 'Biblioteca',
        'arma': 'Candelabro',
        'pista': 'El asesino tiene el cabello rojo.'
    },
    {
        'asesino': 'Green',
        'locacion': 'Cocina',
        'arma': 'Cuchillo',
        'pista': 'El asesino es alérgico al chocolate.'
    },
    {
        'asesino': 'Peacock',
        'locacion': 'Comedor',
        'arma': 'Pistola',
        'pista': 'El asesino tiene un tatuaje en el cuello.'
    },
    {
        'asesino': 'Plum',
        'locacion': 'Estudio',
        'arma': 'Soga',
        'pista': 'El asesino usa lentes de contacto.'
    },
    {
        'asesino': 'Mustard',
        'locacion': 'Salón',
        'arma': 'Tubería',
        'pista': 'El asesino es fanático de la música clásica.'
    }
]

# Escogemos aleatoriamente una historia
historia = random.choice(historias)

# Definimos las pistas del juego
pistas = {
    'asesino': historia['pista'],
    'locacion': 'No hay pistas disponibles por el momento.',
    'arma': 'No hay pistas disponibles por el momento.'
}

print("¡Bienvenido a Clue!")
print("Debes encontrar al asesino, el arma y la locación del crimen.")
print("Las opciones son:")
print("Personajes:", personajes)
print("Locaciones:", locaciones)
print("Armas:", armas)

print("Aquí está la pista inicial:", pistas['asesino'])

# Comenzamos el juego
while True:
    print("¿Qué te gustaría hacer?")
    print("1. Pedir una pista.")
    print("2. Hacer una pregunta.")
    print("3. Hacer una acusación.")
    print("4. Rendirse.")

    opcion = input("Selecciona una opción (1, 2, 3 o 4): ")

    if opcion == "1":
        print("Selecciona una categoría:")
        print("1. Personajes")
        print("2. Locaciones")
        print("3. Armas")
        
        categoria = input("Selecciona una opción (1, 2 o 3): ")
        
        if categoria == "1":
            print(pistas['asesino'])
                
        elif categoria == "2":
            print(pistas['locacion'])
                
        elif categoria == "3":
            print(pistas['arma'])
        
        else:
            print("Opción inválida.")
    
    elif opcion == "2":
        print("Selecciona una categoría:")
        print("1. Personajes")
        print("2. Locaciones")
        print("3. Armas")
    
    categoria = input("Selecciona una opción (1, 2 o 3): ")
    
    if categoria == "1":
        pregunta = input("¿Qué pregunta te gustaría hacer sobre los personajes? ")
        respuesta = historia['asesino'] if pregunta.lower().startswith('quién') else 'No puedo responder esa pregunta.'
        print(respuesta)
            
    elif categoria == "2":
        pregunta = input("¿Qué pregunta te gustaría hacer sobre las locaciones? ")
        respuesta = historia['locacion'] if pregunta.lower().startswith('dónde') else 'No puedo responder esa pregunta.'
        print(respuesta)
            
    elif categoria == "3":
        pregunta = input("¿Qué pregunta te gustaría hacer sobre las armas? ")
        respuesta = historia['arma'] if pregunta.lower().startswith('con qué') else 'No puedo responder esa pregunta.'
        print(respuesta)
    
    else:
        print("Opción inválida.")









       elif opcion == "3":
    asesino = input("¿Quién crees que es el asesino? ")
    locacion = input("¿Dónde crees que fue el crimen? ")
    arma = input("¿Con qué crees que se cometió el crimen? ")
    
    if asesino == historia['asesino'] and locacion == historia['locacion'] and arma == historia['arma']:
        print("¡Felicitaciones! Has encontrado al asesino, el arma y la locación del crimen.")
        break
    else:
        print("Lo siento, esa no es la respuesta correcta.")

elif opcion == "4":
    print("La respuesta era:")
    print("Asesino:", historia['asesino'])
    print("Locación:", historia['locacion'])
    print("Arma:", historia['arma'])
    break

else:
    print("Opción inválida. Por favor, selecciona una opción válida (1, 2, 3 o 4).")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "n":
        break