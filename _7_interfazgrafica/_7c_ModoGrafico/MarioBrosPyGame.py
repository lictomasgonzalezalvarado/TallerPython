import pygame
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Configuración del jugador
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_COLOR = BLUE
GRAVITY = 0.5
JUMP_STRENGTH = -10

# Clase del jugador
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0
        self.on_ground = False

    def update(self, platforms):
        # Movimiento horizontal
        self.rect.x += self.change_x

        # Colisión horizontal
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.change_x > 0:  # Moviendo a la derecha
                    self.rect.right = platform.rect.left
                elif self.change_x < 0:  # Moviendo a la izquierda
                    self.rect.left = platform.rect.right

        # Aplicar gravedad
        self.change_y += GRAVITY
        self.rect.y += self.change_y

        # Colisión vertical
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.change_y > 0:  # Cayendo
                    self.rect.bottom = platform.rect.top
                    self.change_y = 0
                    self.on_ground = True
                elif self.change_y < 0:  # Saltando hacia arriba
                    self.rect.top = platform.rect.bottom
                    self.change_y = 0

    def jump(self):
        if self.on_ground:
            self.change_y = JUMP_STRENGTH

# Clase de la plataforma
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Configuración de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mario Bros - Pygame")

# Reloj para controlar la velocidad de fotogramas
clock = pygame.time.Clock()

# Crear al jugador
player = Player(100, 500)

# Crear plataformas
platforms = [
    Platform(0, SCREEN_HEIGHT - 20, SCREEN_WIDTH, 20),  # Suelo
    Platform(200, 450, 200, 20),  # Plataforma intermedia
    Platform(450, 350, 150, 20),  # Plataforma superior
    Platform(650, 250, 100, 20),  # Plataforma más alta
]

# Agrupar sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
platform_group = pygame.sprite.Group()
for platform in platforms:
    all_sprites.add(platform)
    platform_group.add(platform)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Saltar con la barra espaciadora
                player.jump()

    # Movimiento del jugador con teclas
    keys = pygame.key.get_pressed()
    player.change_x = 0
    if keys[pygame.K_LEFT]:
        player.change_x = -5
    if keys[pygame.K_RIGHT]:
        player.change_x = 5

    # Actualizar al jugador y verificar colisiones
    player.update(platform_group)

    # Dibujar todo
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    clock.tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()
