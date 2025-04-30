import random
import sys, subprocess
import pygame

# Función para borrar lo que diga la terminal
def clearScreen():
    operatingSystem = sys.platform
    if operatingSystem == "win32":
        subprocess.run("cls", shell=True)
    elif operatingSystem in ["linux", "darwin"]:
        subprocess.run("clear", shell=True)


pygame.init()
screen = pygame.display.set_mode((1200, 620))
pygame.display.set_caption("Batalla Naval")

# Fuentes
firstFont = pygame.font.SysFont("Courier New", 15, bold=True)
secondFont = pygame.font.SysFont("Verdana", 28)

page = 0  # Variable global que controla la pantalla actual

# Colores
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (210, 180, 140)
WATER = (0, 102, 204)
SHIP = (34, 139, 34)
CORRECT_SHOT = (255, 69, 0)
INCORRECT_SHOT = (169, 169, 169)
BORDER = (139, 69, 19)
BOARD = (255, 255, 255)
BUTTON = (160, 82, 45)
BUTTON_HOVER = (205, 133, 63)
BUTTON_PRESSED = (139, 69, 19)

# Input de nombre
input_box_filas = pygame.Rect(300, 200, 200, 40)
input_active_filas = False
input_text_filas = ''

input_box_columnas = pygame.Rect(300, 200, 200, 40)
input_active_columnas = False
input_text_columnas = ''

text_lines = [
    "██████╗  █████╗ ████████╗ █████╗ ██╗     ██╗      █████╗   ███╗  ██╗ █████╗ ██╗   ██╗ █████╗ ██╗     ",
    "██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║     ██║     ██╔══██╗  ████╗ ██║██╔══██╗██║   ██║██╔══██╗██║     ",
    "██████╦╝███████║   ██║   ███████║██║     ██║     ███████║  ██╔██╗██║███████║╚██╗ ██╔╝███████║██║     ",
    "██╔══██╗██╔══██║   ██║   ██╔══██║██║     ██║     ██╔══██║  ██║╚████║██╔══██║ ╚████╔╝ ██╔══██║██║     ",
    "██████╦╝██║  ██║   ██║   ██║  ██║███████╗███████╗██║  ██║  ██║ ╚███║██║  ██║  ╚██╔╝  ██║  ██║███████╗",
    "╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝  ╚═╝  ╚══╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝"
]

# Función para mostrar texto
def show_text(textOptions):
    text = secondFont.render(textOptions, True, WHITE)
    screen.blit(text, (125, 125))

# Función para mostrar los inputs con posición controlada por offset
def show_labeled_input(label, base_rect, active, text, events, offset_pos=(0, 0), label_offset=(0, 0)):
    # Colores de los bordes del input
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_active if active else color_inactive

    # Copiamos el input_box con su posición desplazada
    input_box = pygame.Rect(
        base_rect.x + offset_pos[0],
        base_rect.y + offset_pos[1],
        base_rect.w,
        base_rect.h
    )

    # Manejo de eventos
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Si se hace clic en este input, se activa
            if input_box.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_RETURN:
                print(f"{label} ingresado:", text)
                return '', active  # Limpiar texto
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode

    # Dibujar la etiqueta
    label_surface = secondFont.render(f"{label}:", True, WHITE)
    screen.blit(
        label_surface,
        (
            input_box.x - label_surface.get_width() - 10 + label_offset[0],
            input_box.y + label_offset[1]
        )
    )

    # Dibujar el texto del input
    txt_surface = secondFont.render(text, True, WHITE)
    width = max(200, txt_surface.get_width() + 10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(screen, color, input_box, 2)

    return text, active

# Función para mostrar el texto grande
def showBatallaNaval():
    y_position = 100
    for line in text_lines:
        text_surface = firstFont.render(line, True, WHITE)
        screen.blit(text_surface, (125, y_position))
        y_position += 19

# Función para mostrar los botones
def show_button(textChange, positionChange):
    global page
    button = pygame.Rect(positionChange)
    pos_mouse = pygame.mouse.get_pos()
    click_mouse = pygame.mouse.get_pressed()
    if button.collidepoint(pos_mouse):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        button_color = BUTTON_HOVER
        if click_mouse[0]:
            button_color = BUTTON_PRESSED
            if "Salir" in textChange:
                clearScreen()
                pygame.quit()
                sys.exit()
            elif textChange == '1.  One Player':
                page = 1
            elif textChange == '2.  Two Players':
                page = 2
            elif textChange == 'Volver':
                page = 0
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        button_color = BUTTON

    pygame.draw.rect(screen, button_color, button, border_radius=12)
    texto_boton = secondFont.render(textChange, True, WHITE)
    screen.blit(texto_boton, (button.x + 20, button.y + 10))

while True:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)

    if page == 0:
        showBatallaNaval()
        show_button("1.  One Player", (220, 300, 240, 60))
        show_button("2.  Two Players", (500, 300, 245, 60))
        show_button("3.  Salir", (780, 300, 160, 60))
    elif page == 1:
        show_text("Decida las dimensiones del tablero:")
        show_button("Salir", (1050, 520, 105, 60))
        show_button("Volver", (10, 520, 130, 60))
        input_text_filas, input_active_filas = show_labeled_input("Cantidad de filas", input_box_filas, input_active_filas, input_text_filas, eventos)
        input_text_columnas, input_active_columnas = show_labeled_input("Cantidad de columnas", input_box_columnas, input_active_columnas, input_text_columnas, eventos, offset_pos=(75, 50))
    elif page == 2:
        show_text("Decida las dimensiones del tablero:")
        #                      X     Y  ANCHO  ALTO
        show_button("Salir", (1050, 520, 105, 60))
        show_button("Volver", (10, 520, 130, 60))
        input_text_filas, input_active_filas = show_labeled_input("Cantidad de filas", input_box_filas, input_active_filas, input_text_filas, eventos)
        input_text_columnas, input_active_columnas = show_labeled_input("Cantidad de columnas", input_box_columnas, input_active_columnas, input_text_columnas, eventos, offset_pos=(75, 50))

    pygame.display.flip()