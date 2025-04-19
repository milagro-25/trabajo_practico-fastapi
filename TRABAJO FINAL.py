
import pygame
import random

# Inicializar Pygame
pygame.init()

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)

# Tamaño de la ventana
ANCHO = 600
ALTO = 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('La vivorita')

# Reloj
reloj = pygame.time.Clock()

# Tamaño del bloque de la vivorita
bloque = 20

# Fuente para el texto
fuente = pygame.font.SysFont(None, 35)

# Funciones para el récord
def cargar_record():
    try:
        with open("record.txt", "r") as archivo:
            return int(archivo.read())
    except:
        return 0

def guardar_record(nuevo_record):
    with open("record.txt", "w") as archivo:
        archivo.write(str(nuevo_record))

# Mostrar puntaje y récord
def mostrar_puntaje(puntaje, record):
    texto = fuente.render(f"Puntaje: {puntaje}  |  Récord: {record}", True, BLANCO)
    ventana.blit(texto, [10, 10])

# Juego principal
def juego():
    game_over = False
    game_close = False

    x = ANCHO // 2
    y = ALTO // 2

    x_cambio = 0
    y_cambio = 0

    cuerpo_snake = []
    largo_snake = 1

    comida_x = round(random.randrange(0, ANCHO - bloque) / 20.0) * 20.0
    comida_y = round(random.randrange(0, ALTO - bloque) / 20.0) * 20.0

    record = cargar_record()

    while not game_over:

        while game_close:
            ventana.fill(NEGRO)
            mensaje = fuente.render("Perdiste! Q para salir o C para continuar", True, BLANCO)
            ventana.blit(mensaje, [ANCHO // 8, ALTO // 3])
            mostrar_puntaje(largo_snake - 1, record)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        juego()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and x_cambio == 0:
                    x_cambio = -bloque
                    y_cambio = 0
                elif evento.key == pygame.K_RIGHT and x_cambio == 0:
                    x_cambio = bloque
                    y_cambio = 0
                elif evento.key == pygame.K_UP and y_cambio == 0:
                    y_cambio = -bloque
                    x_cambio = 0
                elif evento.key == pygame.K_DOWN and y_cambio == 0:
                    y_cambio = bloque
                    x_cambio = 0

        x += x_cambio
        y += y_cambio

        if x >= ANCHO or x < 0 or y >= ALTO or y < 0:
            game_close = True

        ventana.fill(NEGRO)
        pygame.draw.rect(ventana, ROJO, [comida_x, comida_y, bloque, bloque])

        cabeza = []
        cabeza.append(x)
        cabeza.append(y)
        cuerpo_snake.append(cabeza)

        if len(cuerpo_snake) > largo_snake:
            del cuerpo_snake[0]

        for segmento in cuerpo_snake[:-1]:
            if segmento == cabeza:
                game_close = True

        for parte in cuerpo_snake:
            pygame.draw.rect(ventana, VERDE, [parte[0], parte[1], bloque, bloque])

        mostrar_puntaje(largo_snake - 1, record)
        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, ANCHO - bloque) / 20.0) * 20.0
            comida_y = round(random.randrange(0, ALTO - bloque) / 20.0) * 20.0
            largo_snake += 1

        reloj.tick(10)

    if largo_snake - 1 > record:
        guardar_record(largo_snake - 1)

    pygame.quit()

# Iniciar el juego
juego()
