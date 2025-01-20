import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Aviones Multijugador")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
GRIS = (128, 128, 128)

# Configuración del reloj
reloj = pygame.time.Clock()
FPS = 60

# Fuentes
fuente = pygame.font.Font(None, 36)

# Clases principales
class Avion:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.color = color
        self.velocidad = 5
        self.balas = []

    def mover(self, teclas, arriba, abajo, izquierda, derecha):
        if teclas[arriba] and self.rect.top > 0:
            self.rect.y -= self.velocidad
        if teclas[abajo] and self.rect.bottom < ALTO:
            self.rect.y += self.velocidad
        if teclas[izquierda] and self.rect.left > 0:
            self.rect.x -= self.velocidad
        if teclas[derecha] and self.rect.right < ANCHO:
            self.rect.x += self.velocidad

    def disparar(self, tecla_disparo):
        keys = pygame.key.get_pressed()
        if keys[tecla_disparo]:
            if len(self.balas) < 5:  # Limitar el número de balas en pantalla
                self.balas.append(pygame.Rect(self.rect.centerx - 5, self.rect.top, 10, 20))

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, self.rect)
        for bala in self.balas:
            pygame.draw.rect(pantalla, BLANCO, bala)

class Enemigo:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.velocidad = 2

    def mover(self):
        self.rect.y += self.velocidad
        if self.rect.top > ALTO:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(0, ANCHO - self.rect.width)

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, ROJO, self.rect)

class PowerUp:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, VERDE, self.rect)

# Función para mostrar texto
def mostrar_texto(pantalla, texto, fuente, color, x, y):
    superficie = fuente.render(texto, True, color)
    pantalla.blit(superficie, (x, y))

# Función principal del juego
def juego():
    # Crear jugadores
    jugador1 = Avion(100, ALTO - 60, AZUL)
    jugador2 = Avion(ANCHO - 140, ALTO - 60, VERDE)

    # Crear enemigos y power-ups
    enemigos = [Enemigo(random.randint(0, ANCHO - 40), random.randint(-150, -40)) for _ in range(5)]
    power_ups = [PowerUp(random.randint(0, ANCHO - 30), random.randint(-200, -50))]

    # Variables de nivel y puntajes
    nivel = 1
    puntaje1 = 0
    puntaje2 = 0

    corriendo = True
    while corriendo:
        pantalla.fill(NEGRO)

        # Detectar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        # Obtener teclas presionadas
        teclas = pygame.key.get_pressed()

        # Mover jugadores
        jugador1.mover(teclas, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
        jugador2.mover(teclas, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)

        # Disparar balas
        jugador1.disparar(pygame.K_SPACE)
        jugador2.disparar(pygame.K_RETURN)

        # Mover y dibujar enemigos
        for enemigo in enemigos:
            enemigo.mover()
            enemigo.dibujar(pantalla)

            # Detectar colisiones con balas de jugador 1
            for bala in jugador1.balas:
                if bala.colliderect(enemigo.rect):
                    jugador1.balas.remove(bala)
                    enemigo.rect.y = random.randint(-100, -40)
                    enemigo.rect.x = random.randint(0, ANCHO - enemigo.rect.width)
                    puntaje1 += 1

            # Detectar colisiones con balas de jugador 2
            for bala in jugador2.balas:
                if bala.colliderect(enemigo.rect):
                    jugador2.balas.remove(bala)
                    enemigo.rect.y = random.randint(-100, -40)
                    enemigo.rect.x = random.randint(0, ANCHO - enemigo.rect.width)
                    puntaje2 += 1

        # Mover y dibujar balas
        for bala in jugador1.balas:
            bala.y -= 7
            if bala.bottom < 0:
                jugador1.balas.remove(bala)

        for bala in jugador2.balas:
            bala.y -= 7
            if bala.bottom < 0:
                jugador2.balas.remove(bala)

        # Dibujar jugadores
        jugador1.dibujar(pantalla)
        jugador2.dibujar(pantalla)

        # Mover y dibujar power-ups
        for power_up in power_ups:
            power_up.rect.y += 2
            power_up.dibujar(pantalla)

            # Detectar colisión con jugadores
            if power_up.rect.colliderect(jugador1.rect):
                power_ups.remove(power_up)
                power_ups.append(PowerUp(random.randint(0, ANCHO - 30), random.randint(-200, -50)))
                puntaje1 += 5

            elif power_up.rect.colliderect(jugador2.rect):
                power_ups.remove(power_up)
                power_ups.append(PowerUp(random.randint(0, ANCHO - 30), random.randint(-200, -50)))
                puntaje2 += 5

        # Mostrar puntajes y nivel
        mostrar_texto(pantalla, f"Jugador 1: {puntaje1}", fuente, BLANCO, 10, 10)
        mostrar_texto(pantalla, f"Jugador 2: {puntaje2}", fuente, BLANCO, ANCHO - 200, 10)
        mostrar_texto(pantalla, f"Nivel: {nivel}", fuente, BLANCO, ANCHO // 2 - 50, 10)

        # Cambiar nivel
        if puntaje1 + puntaje2 >= nivel * 10:
            nivel += 1
            enemigos.append(Enemigo(random.randint(0, ANCHO - 40), random.randint(-150, -40)))

        # Actualizar pantalla y reloj
        pygame.display.flip()
        reloj.tick(FPS)

# Función para mostrar ayuda
def mostrar_ayuda():
    corriendo = True
    while corriendo:
        pantalla.fill(NEGRO)
        mostrar_texto(pantalla, "Ayuda", fuente, BLANCO, ANCHO // 2 - 50, 50)
        mostrar_texto(pantalla, "Jugador 1:", fuente, BLANCO, 50, 150)
        mostrar_texto(pantalla, "Moverse: W, A, S, D", fuente, GRIS, 50, 200)
        mostrar_texto(pantalla, "Disparar: Espacio", fuente, GRIS, 50, 250)

        mostrar_texto(pantalla, "Jugador 2:", fuente, BLANCO, 50, 350)
        mostrar_texto(pantalla, "Moverse: Flechas", fuente, GRIS, 50, 400)
        mostrar_texto(pantalla, "Disparar: Enter", fuente, GRIS, 50, 450)

        mostrar_texto(pantalla, "Presione ESC para volver al menú", fuente, GRIS, 50, 550)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    corriendo = False

# Menú principal
def menu():
    opcion_actual = 0
    opciones = ["Jugar", "Ayuda", "Salir"]

    corriendo = True
    while corriendo:
        pantalla.fill(NEGRO)
        mostrar_texto(pantalla, "Juego de Aviones Multijugador", fuente, BLANCO, ANCHO // 2 - 200, 50)

        for idx, opcion in enumerate(opciones):
            color = BLANCO if idx == opcion_actual else GRIS
            mostrar_texto(pantalla, opcion, fuente, color, ANCHO // 2 - 50, 150 + idx * 50)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and opcion_actual > 0:
                    opcion_actual -= 1
                elif evento.key == pygame.K_DOWN and opcion_actual < len(opciones) - 1:
                    opcion_actual += 1
                elif evento.key == pygame.K_RETURN:
                    if opcion_actual == 0:
                        juego()
                    elif opcion_actual == 1:
                        mostrar_ayuda()
                    elif opcion_actual == 2:
                        pygame.quit()
                        sys.exit()

menu()
