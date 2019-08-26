#! /usr/bin/env python3
from nota import Nota
class Anotador:
    '''Representa una colección de Notas que se pueden etiquetar, modificar, y
    buscar'''

    def __init__(self):
        '''Inicializa el anotador con una lista vacía de Notas'''
        self.notas = []

    def nueva_nota(self, texto, etiquetas = ''):
        '''Crea una nueva nota y la agrega a la lista'''
        self.notas.append(Nota(texto,etiquetas))

    def _buscar_por_id(self,id_nota):
        '''Buscar la nota con el id dado'''
        for nota in self.notas:
            if str(nota.id) == str(id_nota):
                return nota
        return None

    def modificar_nota(self, id_nota, texto):
        '''Busca la nota con el id dado y modifica el texto'''
        nota = self._buscar_por_id(id_nota)
        if nota:
            nota.texto = texto
            return True
        return False

    def modificar_etiquetas(self, id_nota, etiquetas):
        '''Busca la nota con el id dado y modifica las etiquetas'''
        nota = self._buscar_por_id(id_nota)
        if nota:
            nota.etiquetas = etiquetas
            return True
        return False

    def buscar(self, filtro):
        '''Busca todas las notas que coincidan con el filtro dado'''
        return [ nota for nota in self.notas if nota.coincide(filtro) ]
