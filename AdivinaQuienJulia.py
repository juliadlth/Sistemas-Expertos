import json

# Leer el archivo JSON que contiene la información del modelo
with open("modelo.json", "r") as f:
    modelo = json.load(f)

# Definir los atributos que el modelo usará para adivinar el personaje secreto
atributos = ["genero", "color de pelo", "lentes", "color de piel"]

# Función para adivinar el personaje secreto
def adivinar_personaje(posibles_personajes):
    while len(posibles_personajes) > 1:
        # Iterar sobre cada atributo del modelo
        for atributo in atributos:
            # Preguntar al usuario si el personaje secreto tiene ese atributo
            respuesta = input("¿El personaje secreto tiene {}? ".format(atributo))
        
            # Filtrar la lista de personajes posibles según la respuesta del usuario
            posibles_personajes = [p for p in posibles_personajes if p[atributo].lower() == respuesta.lower()]
        
            # Si no quedan personajes posibles, pedir al usuario que añada el personaje secreto
            if not posibles_personajes:
                print("No conozco ese personaje. Por favor, añádelo.")
                # Crear un nuevo personaje y añadirlo a la lista de personajes
                personaje = {}
                for atributo in atributos:
                    respuesta = input("{}: ".format(atributo))
                    personaje[atributo] = respuesta
                personaje["nombre"] = input("Nombre del personaje: ")
                personajes.append(personaje)
                # Añadir el nuevo personaje al modelo
                for atributo, valor in personaje.items():
                    if valor not in modelo[atributo]:
                        modelo[atributo].append(valor)
                # Guardar el modelo actualizado en el archivo JSON
                with open("modelo.json", "w") as f:
                    json.dump(modelo, f)
                # Reiniciar el juego
                posibles_personajes = personajes[:]
    
    # Mostrar el personaje final
    personaje_final = posibles_personajes[0]
    print("El personaje secreto es: {}".format(personaje_final["nombre"]))


# Ejecutar
if __name__ == "__main__":

    # Inicializar la lista de personajes posibles
    personajes = modelo["personajes"]
    posibles_personajes = personajes[:]
    
    # Preguntar al usuario si quiere jugar
    jugar = input("¿Quieres jugar que adivine tu personaje? (si/no)")
    print("Recuerda que para el genero lo puedes seleccionar como (f/m/o) ,color de piel (moreno/blanco/moreno claro),y los demas ingresa los colores")
    while jugar.lower() == "si":
        adivinar_personaje(posibles_personajes)
        jugar = input("¿Quieres seguir jugando? ")
