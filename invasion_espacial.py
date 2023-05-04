"""
Juego Invasión Espacial
"""
import random
import math
import pygame
from pygame import mixer

# Iniciar Pygame - si no se hace de ésta manera, todas marcan error
pygame.init = pygame.init
pygame.QUIT = pygame.QUIT
pygame.KEYDOWN = pygame.KEYDOWN
pygame.KEYUP = pygame.KEYUP
pygame.K_ESCAPE = pygame.K_ESCAPE
pygame.K_LEFT = pygame.K_LEFT
pygame.K_RIGHT = pygame.K_RIGHT
pygame.K_SPACE = pygame.K_SPACE
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))
fondo = pygame.image.load("fondo-02.jpg")

# Título e Icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni-02.png")
pygame.display.set_icon(icono)

# Agregar Música
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Variables del Jugador
img_jugador = pygame.image.load("cohete-02.png")
jugador_x = 368
jugador_y = 515
jugador_x_movimiento = 0

# Variables del Enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_movimiento = []
enemigo_y_movimiento = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo-02.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(15, 200))
    enemigo_x_movimiento.append(0.3)
    enemigo_y_movimiento.append(50)
    # enemigo_x[e] = random.randint(0, 736)
    # enemigo_y[e] = random.randint(15, 200)
    # enemigo_x_movimiento[e] = 0.3
    # enemigo_y_movimiento[e] = 50

# Variables del Bala
img_bala = pygame.image.load("bala-01.png")
bala_x = 0
bala_y = 500
bala_x_movimiento = 0
bala_y_movimiento = 3
bala_visible = False

# Variable para Puntaje
puntaje = 0
mayor_puntaje = 0
fuente = pygame.font.Font("AunchantedXspace-Bold.ttf", 32)
texto_x = 10
texto_y = 10
texto_mayor_puntaje = pygame.font.Font("AunchantedXspace-Bold.ttf", 32)
texto_pregunta = pygame.font.Font("AunchantedXspace-Bold.ttf", 32)

# Texto Final del Juego
fuente_final = pygame.font.Font("AunchantedXspace-Bold.ttf", 40)

# Función para reiniciar el juego


def reiniciar_juego():
    """Función para reiniciar el juego"""
    global puntaje, enemigo_x, enemigo_y, jugador_x, jugador_y, dificultad, enemigo_x_movimiento
    global enemigo_y_movimiento
    puntaje = 0
    dificultad = 0
    enemigo_x = []
    enemigo_y = []
    enemigo_x_movimiento = []
    enemigo_y_movimiento = []
    jugador_x = 368
    jugador_y = 515
    pygame.display.flip()

# Función para el texto de Fin del Juego


def texto_final():
    """Función para el texto de Fin del Juego"""
    global se_ejecuta
    fin_juego = fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(fin_juego, (250, 200))
    puntaje_mayor = texto_mayor_puntaje.render(
        f"Mayor puntaje: {mayor_puntaje}", True, (255, 255, 255))
    pantalla.blit(puntaje_mayor, (300, 250))
    # Reiniciar Juego
    pregunta = texto_pregunta.render(
        "Para volver a comenzar", True, (255, 255, 255))
    pantalla.blit(pregunta, (255, 300))
    pregunta_1 = texto_pregunta.render(
        "presione cualquier tecla", True, (255, 255, 255))
    pantalla.blit(pregunta_1, (255, 350))
    pygame.display.flip()

    esperar_tecla = True
    while esperar_tecla:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                se_ejecuta = False
                esperar_tecla = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    se_ejecuta = False
                    esperar_tecla = False
                else:
                    reiniciar_juego()
                    esperar_tecla = False

# Función para mostrar el Puntaje


def mostrar_puntaje(x01, y01):
    """Función para mostrar el Puntaje"""
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x01, y01))


# Variable para aumentar la dificultad automáticamente
dificultad = 0

# Función Jugador


def jugador(x01, y01):
    """Función para el Jugador"""
    pantalla.blit(img_jugador, (x01, y01))

# Función Enemigo


def enemigo(x01, y01, ene):
    """Función para el Enemigo"""
    pantalla.blit(img_enemigo[ene], (x01, y01))

# Función Bala


def disparar_bala(x01, y01):
    """Función para disparar la Bala"""
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x01 + 16, y01 + 10))

# Función para detectar colisiones


def hay_colision(x_1, y_1, x_2, y_2):
    """Función para detectar colisiones (D=((X2-X1)^2+(Y2-Y1)^2)^1/2)"""
    distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # Imagen de Fondo
    pantalla.blit(fondo, (0, 0))

    # Guardar el mayor puntaje
    if puntaje > mayor_puntaje:
        mayor_puntaje = puntaje

    # Iterar Eventos
    for evento in pygame.event.get():
        # Evento Cerrar Programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento Presionar Teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_movimiento = -0.4
            if evento.key == pygame.K_RIGHT:
                jugador_x_movimiento = +0.4
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    sonido_bala = mixer.Sound("disparo.mp3")
                    sonido_bala.play()
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        # Evento Soltar Flechas
        if evento.type == pygame.KEYUP:
            # if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
            if evento.key in (pygame.K_LEFT, pygame.K_RIGHT):
                jugador_x_movimiento = 0

    # Modificar Ubicación del Jugador
    jugador_x += jugador_x_movimiento

    # Mantener al Jugador dentro de los bordes
    if jugador_x <= 0:
        jugador_x = 736  # Si colocamos "0" topa en el borde izquierdo
    elif jugador_x >= 736:
        jugador_x = 0  # Si colocamos "736" topa en el borde derecho

    # Modificar Ubicación del Enemigo
    for e in range(cantidad_enemigos):
        # Fin del Juego
        if enemigo_y[e] > 460:
            nave_impactada = True
            sonido_colision = mixer.Sound("explosion-02.mp3")
            sonido_colision.play()
            if not nave_impactada:
                puntaje += 1
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            # break

        enemigo_x[e] += enemigo_x_movimiento[e]

        # Mantener al Enemigo dentro de los bordes
        if enemigo_x[e] <= 0:
            enemigo_x_movimiento[e] = 0.2 + dificultad
            enemigo_y[e] += enemigo_y_movimiento[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_movimiento[e] = -0.2 - dificultad
            enemigo_y[e] += enemigo_y_movimiento[e]
        dificultad += 0.0000001

        # Colisión
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound("explosion-01.mp3")
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(15, 200)

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Movimiento de la Bala
    if bala_y <= -64:
        bala_y = 515
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_movimiento

    jugador(jugador_x, jugador_y)

    mostrar_puntaje(texto_x, texto_y)

    # Actualizar
    pygame.display.update()
