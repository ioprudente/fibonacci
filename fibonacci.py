import pygame
import math

pygame.init()

# Tela
infoObject = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Espiral Dourada com Linha Trajetória")

# Fonte
font = pygame.font.SysFont("Segoe UI", 24, bold=True)

# Cores
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
GLOW = (255, 255, 100)
RADAR = (0, 255, 180)
BG_TOP = (5, 5, 20)
BG_BOTTOM = (10, 10, 40)

# Constantes da espiral
phi = (1 + 5 ** 0.5) / 2
b = math.log(phi) / (math.pi / 2)
a = 1

# Parâmetros
theta = 0
theta_step = 0.005
iterations = 0
max_radius_px = 350

# Lista para armazenar os pontos da espiral
trail_points = []

# Desenha fundo gradiente
def draw_background():
    for y in range(HEIGHT):
        r = BG_TOP[0] + (BG_BOTTOM[0] - BG_TOP[0]) * y // HEIGHT
        g = BG_TOP[1] + (BG_BOTTOM[1] - BG_TOP[1]) * y // HEIGHT
        b = BG_TOP[2] + (BG_BOTTOM[2] - BG_TOP[2]) * y // HEIGHT
        pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))

draw_background()

# Calcula limite da espiral
theta_final = math.log(max_radius_px / a) / b

# Loop principal
running = True
clock = pygame.time.Clock()

while running:
    center_x = screen.get_width() // 2
    center_y = screen.get_height() // 2

    scale = max_radius_px / (a * math.exp(b * theta_final))
    r = a * math.exp(b * theta)
    r_scaled = r * scale

    x = center_x + r_scaled * math.cos(theta)
    y = center_y + r_scaled * math.sin(theta)

    if theta <= theta_final:
        # Adiciona novo ponto à trilha
        trail_points.append((int(x), int(y)))

        # Pontinho da espiral
        pygame.draw.circle(screen, GLOW, (int(x), int(y)), 5)
        pygame.draw.circle(screen, GOLD, (int(x), int(y)), 2)

        iterations += 1

    # Redesenha trilha da espiral (linha amarela contínua)
    if len(trail_points) > 1:
        pygame.draw.lines(screen, GOLD, False, trail_points, 2)

    # Linha radar (só sobreposta)
    if theta <= theta_final:
        radar_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.line(
            radar_surface,
            (*RADAR, 180),
            (center_x, center_y),
            (int(x), int(y)),
            3
        )
        screen.blit(radar_surface, (0, 0))

    # HUD
    hud_surface = pygame.Surface((300, 70), pygame.SRCALPHA)
    pygame.draw.rect(hud_surface, (0, 0, 0, 180), (0, 0, 300, 70), border_radius=12)
    text1 = font.render(f"Iterações: {iterations}", True, WHITE)
    text2 = font.render(f"Raio: {round(r_scaled, 1)} px", True, WHITE)
    hud_surface.blit(text1, (15, 10))
    hud_surface.blit(text2, (15, 40))
    screen.blit(hud_surface, (20, 20))

    pygame.display.update()
    theta += theta_step
    clock.tick(240)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            draw_background()
            trail_points = []

pygame.quit()
