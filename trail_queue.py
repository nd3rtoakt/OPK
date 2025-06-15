import pygame

class Trail:
    pass

def create_trail():
    return {'points': [], 'max_length': 100}

def add_trail_point(trail, x, y, color):
    trail['points'].append((x, y, color))
    if len(trail['points']) > trail['max_length']:
        trail['points'].pop(0)

def draw_trail(trail, surface):
    for i, (x, y, color) in enumerate(trail['points']):
        alpha = int(255 * i / len(trail['points']))
        faded_color = (max(0, color[0]-50), max(0, color[1]-50), max(0, color[2]-50), alpha)
        pygame.draw.circle(surface, faded_color, (int(x), int(y)), 1)