
from anuncio import Video, Display, Social 

class LargoExcedidoException(Exception):
    pass

class Campaña:  # Nombre de la clase Campaña
    def __init__(self, nombre, anuncios):  # Metodo de Instancia de inicio
        self._nombre = nombre              # Atributos de la clase
        self._anuncios = anuncios

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if len(value) <= 250:
            self._nombre = value
        else:
            raise LargoExcedidoException("El nombre de la campaña no puede superar los 250 caracteres.")

    @property
    def anuncios(self):
        return self._anuncios

    def __str__(self):
        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {len(self.anuncios)} Video, {len(self.anuncios)} Display, {len(self.anuncios)} Social"
    

