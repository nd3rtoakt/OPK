import pygame
from physics import calculate_gravity, update_position, update_velocity, calculate_initial_velocity
from trail_queue import create_trail, add_trail_point, draw_trail
from bodies import Body, create_body, draw_body

pygame.init()

WIDTH, HEIGHT = 1500, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Планетная система")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PLANET_COLORS = [
    (100, 100, 255),  # Голубой
    (255, 100, 100),  # Красный
    (100, 255, 100),  # Зеленый
    (255, 255, 100),  # Желтый
    (100, 255, 255),  # Бирюзовый
    (255, 100, 255)   # Розовый
]


G = 6.67430e-11 * 1e10


def create_solar_system():
    bodies = []
    sun = create_body(WIDTH // 2, HEIGHT // 2, 1000, YELLOW, is_star=True, name="Солнце")
    sun['fixed'] = True
    bodies.append(sun)

    earth = create_body(WIDTH // 2 + 150, HEIGHT // 2, 10, BLUE, name="Земля")
    earth['vx'], earth['vy'] = calculate_initial_velocity(earth, sun, G)
    bodies.append(earth)

    mars = create_body(WIDTH // 2 + 200, HEIGHT // 2, 6, RED, name="Марс")
    mars['vx'], mars['vy'] = calculate_initial_velocity(mars, sun, G)
    bodies.append(mars)

    return bodies


def draw_help(screen):
    font = pygame.font.Font(None, 24)
    instructions = [
        "Управление:",
        "ЛКМ - добавить планету",
        "Пробел - пауза/продолжить",
        "R - сбросить систему",
        "+/- - изменить скорость",
        "ESC - закрыть подсказку"
    ]


    pygame.draw.rect(screen, (30, 30, 30), (10, 10, 250, 30 + len(instructions) * 25))

    for i, instruction in enumerate(instructions):
        text = font.render(instruction, True, WHITE)
        screen.blit(text, (20, 15 + i * 25))


def draw_ui(screen, paused, simulation_speed, editing_planet):
    font = pygame.font.Font(None, 24)


    text = font.render(f"Скорость: {simulation_speed:.1f}x", True, WHITE)
    screen.blit(text, (WIDTH - 150, 15))


    if editing_planet:

        pygame.draw.rect(screen, GRAY, (editing_planet['x'] + 50, editing_planet['y'] - 60, 200, 80))


        pygame.draw.rect(screen, BLACK, (editing_planet['x'] + 60, editing_planet['y'] - 50, 180, 30))
        name_text = font.render(f"Имя: {editing_planet['name']}", True, WHITE)
        screen.blit(name_text, (editing_planet['x'] + 65, editing_planet['y'] - 45))


        pygame.draw.rect(screen, (0, 200, 0), (editing_planet['x'] + 130, editing_planet['y'] - 10, 60, 30))
        confirm_text = font.render("OK", True, WHITE)
        screen.blit(confirm_text, (editing_planet['x'] + 150, editing_planet['y'] - 5))


def main():
    clock = pygame.time.Clock()
    bodies = create_solar_system()
    paused = False
    simulation_speed = 1.0
    dt = 0.1

    editing_planet = None
    current_input = ""
    input_mode = False
    color_index = 0
    show_help = True

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if editing_planet:

                    x, y = editing_planet['x'] + 50, editing_planet['y'] - 60


                    if x + 60 <= mouse_pos[0] <= x + 240 and y + 10 <= mouse_pos[1] <= y + 40:
                        input_mode = True
                        current_input = editing_planet['name']


                    elif x + 130 <= mouse_pos[0] <= x + 190 and y + 50 <= mouse_pos[1] <= y + 80:
                        paused = False
                        editing_planet = None
                        input_mode = False
                else:
                    star = next(body for body in bodies if body['is_star'])
                    dist = ((mouse_pos[0] - star['x']) ** 2 + (mouse_pos[1] - star['y']) ** 2) ** 0.5

                    if dist > 50:
                        color = PLANET_COLORS[color_index % len(PLANET_COLORS)]
                        color_index += 1

                        new_planet = create_body(
                            mouse_pos[0], mouse_pos[1],
                            10,
                            color,
                            name=f"Планета {len(bodies)}"
                        )

                        new_planet['vx'], new_planet['vy'] = calculate_initial_velocity(new_planet, star, G)

                        paused = True
                        editing_planet = new_planet
                        bodies.append(new_planet)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    show_help = not show_help

                elif input_mode and editing_planet:
                    if event.key == pygame.K_RETURN:
                        editing_planet['name'] = current_input
                        input_mode = False
                    elif event.key == pygame.K_BACKSPACE:
                        current_input = current_input[:-1]
                    else:
                        current_input += event.unicode
                else:
                    if event.key == pygame.K_SPACE:
                        paused = not paused
                    elif event.key == pygame.K_r:
                        bodies = create_solar_system()
                        paused = False
                        editing_planet = None
                        color_index = 0
                    elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                        simulation_speed *= 1.5
                    elif event.key == pygame.K_MINUS:
                        simulation_speed /= 1.5

        if input_mode and editing_planet:
            editing_planet['name'] = current_input

        if not paused and not editing_planet:
            for _ in range(int(simulation_speed)):
                for i, body1 in enumerate(bodies):
                    if body1.get('fixed', False):
                        continue
                    fx_total, fy_total = 0, 0
                    for j, body2 in enumerate(bodies):
                        if i != j:
                            fx, fy = calculate_gravity(body1, body2, G)
                            fx_total += fx
                            fy_total += fy
                    update_velocity(body1, fx_total, fy_total, dt)

                for body in bodies:
                    if not body.get('fixed', False):
                        update_position(body, dt)
                    if not body['is_star']:
                        add_trail_point(body['trail'], body['x'], body['y'], body['color'])

        screen.fill(BLACK)

        for body in bodies:
            if not body['is_star']:
                draw_trail(body['trail'], screen)

        for body in bodies:
            draw_body(body, screen)

        draw_ui(screen, paused, simulation_speed, editing_planet)

        if show_help:
            draw_help(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()