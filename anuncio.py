
from abc import ABC, abstractmethod

class SubTipoInvalidoException(Exception):
    pass

class Anuncio(ABC): # Nombre de la Classe Abstracta Anuncio
    def __init__(self, alto=1, ancho=1, sub_tipo=None, url_archivo=None, url_clic=None): # Atributos de la Classe
        self._alto = alto if alto > 0 else 1
        self._ancho = ancho if ancho > 0 else 1
        self._sub_tipo = sub_tipo
        self._url_archivo = url_archivo
        self._url_clic = url_clic

    @abstractmethod    # Se define el Método abstractos implementados por las sub-clase
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass

    @staticmethod     # Se define el metodo estático que imprime los formatos disponibles
    def mostrar_formatos():
        print("FORMATOS DISPONIBLES:")
        print("====================")
        print("Video: mp4, avi")
        print("Display: jpg, png")
        print("Social: Facebook, Instagram, Twitter")

class Video(Anuncio): # Sub-Clase de Anuncio
    def __init__(self, duracion=5, formato="mp4"):
        super().__init__(alto=1, ancho=1)
        self._duracion = duracion if duracion > 0 else 5  # atributos de la clase
        self._formato = formato

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio): # Sub-clase de Anuncio con sus respectivos atributos
    def __init__(self, formato="jpg"):
        super().__init__()
        self._formato = formato

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

    
class Social(Anuncio): # Sub- clase de Anuncio con sus respectivos atributos y metodo abstracto de la clase Anuncio 
    def __init__(self, plataforma="Facebook"):
        super().__init__()
        self._plataforma = plataforma

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
 
   


