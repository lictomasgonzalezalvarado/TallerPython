
import pygame

if __name__ == '__main__':
    print("Reprodudiendo Rolling in the Deep con los Vazquez Boys")
    # Inicializar el mixer de pygame
    pygame.mixer.init()

    # Cargar y reproducir el archivo MP3
    pygame.mixer.music.load("F:\\Docencia ITSSMT\\AGO-DIC 2024\\Arq de Comp\\TallerPyton\\_8_net\\_8c_TransferenciasArchivosPOO\\adelecover.mp3")
    pygame.mixer.music.play()

    # Mantener el programa activo mientras suena la música
    while pygame.mixer.music.get_busy():
        continue

    print("Fin de la reproducción")