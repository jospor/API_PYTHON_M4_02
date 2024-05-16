from campaña import Campaña
from anuncio import Video, Display, Social
from error import SubTipoInvalidoException, LargoExcedidoException


def crear_campaña():
    nombre = input("Ingrese el nombre de la campaña: ")

    duracion_video = int(input("Ingrese la duración del video: "))
    formato_video = input("Ingrese el formato del video: ")
    video = Video(duracion=duracion_video, formato=formato_video)

    formato_display = input("Ingrese el formato del display: ")
    display = Display(formato=formato_display)

    plataforma_social = input("Ingrese la plataforma social: ")
    social = Social(plataforma=plataforma_social)

    anuncios = [video, display, social]
    campaña = Campaña(nombre=nombre, anuncios=anuncios)

    return campaña


def gestionar_campaña(campaña):
    nuevo_nombre = input("Ingrese un nuevo nombre para la campaña: ")
    try:
        campaña.nombre = nuevo_nombre
    except LargoExcedidoException as e:
        with open("error.log", "a") as f:
            f.write(str(e))

    nuevo_sub_tipo = input("Ingrese un nuevo subtipo para el anuncio de video: ")
    try:
        campaña.anuncios[0].sub_tipo = nuevo_sub_tipo
    except SubTipoInvalidoException as e:
        with open("error.log", "a") as f:
            f.write(str(e))

campaña = crear_campaña()
gestionar_campaña(campaña)
