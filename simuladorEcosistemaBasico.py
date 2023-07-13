import matplotlib.pyplot as plt
import random

class Organismo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.poblacion = 100
        self.capacidad_reproduccion = 0.8
        self.tasa_mortalidad = 0.2

    def reproducirse(self):
        hijos = int(self.poblacion * self.capacidad_reproduccion)
        hijos = random.randint(1, hijos)
        self.poblacion += hijos

    def morir(self):
        muertes = int(self.poblacion * self.tasa_mortalidad)
        muertes = random.randint(1, muertes)
        self.poblacion -= muertes

def simular_ecosistema(num_generaciones):
    organismos = [Organismo('Organismo 1'), Organismo('Organismo 2'), Organismo('Organismo 3')]
    poblaciones = [[] for _ in organismos]

    for generacion in range(num_generaciones):
        for index, organismo in enumerate(organismos):
            organismo.reproducirse()
            organismo.morir()
            poblaciones[index].append(organismo.poblacion)

    for index, organismo in enumerate(organismos):
        plt.plot(poblaciones[index], label=organismo.nombre)

    plt.xlabel('Generaciones')
    plt.ylabel('Población')
    plt.title('Evolución de la población de organismos')
    plt.legend()
    plt.show()

# Ejemplo de uso
simular_ecosistema(100)
