def calculate_gravity(body1, body2, G):
    dx = body2['x'] - body1['x']
    dy = body2['y'] - body1['y']
    distance_sq = dx*dx + dy*dy
    if distance_sq == 0:
        return 0, 0
    distance = distance_sq**0.5
    force = G * body1['mass'] * body2['mass'] / distance_sq
    fx = force * dx / distance
    fy = force * dy / distance
    return fx, fy

def update_velocity(body, fx, fy, dt):
    body['vx'] += fx / body['mass'] * dt
    body['vy'] += fy / body['mass'] * dt

def update_position(body, dt):
    body['x'] += body['vx'] * dt
    body['y'] += body['vy'] * dt

def calculate_initial_velocity(body, star, G):
    dx = body['x'] - star['x']
    dy = body['y'] - star['y']
    distance = (dx*dx + dy*dy)**0.5
    if distance == 0:
        return 0, 0
    orbital_speed = (G * star['mass'] / distance)**0.5
    direction = 1 if (body['x']*body['y'] > 0) else -1  # Простое определение направления
    vx = -direction * orbital_speed * dy / distance
    vy = direction * orbital_speed * dx / distance
    return vx, vy