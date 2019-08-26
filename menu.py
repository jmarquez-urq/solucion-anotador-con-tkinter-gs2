#! /usr/bin/env python3
from anotador import Anotador
import sys
class Menu:
    '''Mostrar un menú y responder a las opciones'''
    def __init__(self):
        self.anotador = Anotador()
        self.opciones= {
            "1": self.mostrar_notas,
            "2": self.buscar_notas,
            "3": self.agregar_nota,
            "4": self.modificar_nota,
            "5": self.salir
        }

    def mostrar_menu(self):
        print("""
Menú del anotador:
1. Mostrar todas las notas
2. Buscar Notas
3. Agregar Nota
4. Modificar Nota
5. Salir
""")

    def ejecutar(self):
        '''Mostrar el menu y responder a las opciones.'''
        while True:
            self.mostrar_menu()
            opcion = input("Ingresar una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("{0} no es una opción válida".format(opcion))

    def mostrar_notas(self, notas=None):
        if not notas:
            notas = self.anotador.notas
        for nota in notas:
            print("{0}: {1}\n{2}".format(nota.id, nota.etiquetas, nota.texto))
    
    def buscar_notas(self):
        filtro = input("Buscar: ")
        notas = self.anotador.buscar(filtro)
        if notas:
            self.mostrar_notas(notas)
        else:
            print("Ninguna nota coincide con la búsqueda")
    
    def agregar_nota(self):
        texto = input("Ingrese el texto de la nota: ")
        self.anotador.nueva_nota(texto)
        print("Su nota ha sido añadida.")

    def modificar_nota(self):
        id = input("Ingrese el id de la nota a modificar: ")
        texto = input("Ingrese el texto de la nota: ")
        etiquetas = input("Ingrese las etiquetas: ")
        if texto:
            self.anotador.modificar_nota(id, texto)
        if etiquetas:
            self.anotador.modificar_etiquetas(id, etiquetas)
    
    def salir(self):
        print("Gracias por utilizar el sistema.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().ejecutar()
