import pygame
from trail_queue import create_trail, add_trail_point, draw_trail

class body:
    pass

def create_body(x, y, mass, color, is_star=False, name=""):
    body = {
        'x': x,
        'y': y,
        'mass': mass,
        'vx': 0,
        'vy': 0,
        'color': color,
        'radius': int(mass**0.33) if not is_star else 30,
        'is_star': is_star,
        'name': name,
        'trail': create_trail(),
        'fixed': is_star
    }
    return body

def draw_body(body, surface):
    pygame.draw.circle(surface, body['color'], (int(body['x']), int(body['y'])), body['radius'])
    if body['name']:
        font = pygame.font.Font(None, 20)
        text = font.render(body['name'], True, (255, 255, 255))
        surface.blit(text, (int(body['x']) + body['radius'] + 5, int(body['y']) - 10))
