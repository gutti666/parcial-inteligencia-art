import pandas as pd

# Diccionario que mapea el nombre del animal con su número
mapa_animales = {
    "Ballena": 0, "Carnero": 1, "Toro": 2, "Ciempiés": 3, "Alacrán": 4,
    "León": 5, "Ranas": 6, "Perico": 7, "Ratón": 8, "Águila": 9, "Tigre": 10, "Gato": 11,
    "Caballo": 12, "Mono": 13, "Paloma": 14, "Zorro": 15, "Oso": 16, "Pavo": 17, "Burro": 18,
    "Chivo": 19, "Cochino": 20, "Gallo": 21, "Camello": 22, "Cebra": 23, "Iguana": 24, 
    "Gallina": 25, "Vaca": 26, "Perro": 27, "Zamuro": 28, "Elefante": 29, "Caimán": 30,
    "Lapa": 31, "Ardilla": 32, "Pescado": 33, "Venado": 34, "Jirafa": 35, "Culebra": 36,
    "Tortuga": 37, "Búfalo": 38, "Lechuza": 39, "Avispa": 40, "Canguro": 41, "Tucán": 42,
    "Mariposa": 43, "Chigüire": 44, "Garza": 45, "Puma": 46, "Pavo Real": 47, 
    "Puercoespín": 48, "Pereza": 49, "Canario": 50, "Pelícano": 51, "Pulpo": 52, 
    "Caracol": 53, "Grillo": 54, "Oso Hormiguero": 55, "Tiburón": 56, "Pato": 57, 
    "Hormiga": 58, "Pantera": 59, "Camaleón": 60, "Panda": 61, "Cachicamo": 62, 
    "Cangrejo": 63, "Gavilán": 64, "Araña": 65, "Lobo": 66, "Avestruz": 67, "Jaguar": 68, 
    "Conejo": 69, "Bisonte": 70, "Guacamaya": 71, "Gorila": 72, "Hipopótamo": 73, 
    "Turpial": 74, "Guácharo": 75
}

# Leer el archivo de resultados (se asume que el archivo está en el formato adecuado)
with open("resultados_guacharoactivo_2024.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

# Procesar las líneas para extraer la información
datos = []
for linea in lineas:
    # Filtrar las líneas vacías o irrelevantes
    if linea.strip():
        partes = linea.strip().split(",")
        if len(partes) == 3:
            fecha, hora, animalito = partes
            # Homologar el número del animal según el diccionario
            numero = mapa_animales.get(animalito.strip(), None)
            if numero is not None:
                datos.append([fecha, hora, animalito.strip(), numero])