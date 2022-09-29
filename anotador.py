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
        nota = Nota(texto,etiquetas)
        self.notas.append(nota)
        return nota

    def _buscar_por_id(self,id_nota):
        '''Buscar la nota con el id dado'''
        for nota in self.notas:
            if str(nota.id) == str(id_nota):
                return nota
        return None

    def buscar(self, filtro):
        '''Busca todas las notas que coincidan con el filtro dado'''
        notas_que_coinciden = []
        for nota in self.notas:
            if nota.coincide(filtro):
                notas_que_coinciden.append(nota)
        return notas_que_coinciden

    def eliminar_nota(self,id_nota):
        '''Busca la nota con el id dado y la elimina'''
        nota = self._buscar_por_id(id_nota)
        if nota:
            self.notas.remove(nota)
            return True
        return False

    def modificar(self, id_nota, texto, etiquetas):
        nota = self._buscar_por_id(id_nota)
        if nota:
            nota.texto = texto
            nota.etiquetas = etiquetas
            return True
        return False

