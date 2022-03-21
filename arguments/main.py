# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
import re

def greet(name, template = 'Hello, <name>!'):
    if template == 'Hello, <name>!':
        return f"Hello, {name}!"
    else:
        result = (re.sub('<name>', f"{name}", template))  
        return result

print('Steven')

def force(mass: float, body: str = '<earth>!'):
    planet = {'sun': 274,
    'jupiter': 24.92,
    'neptune': 11.15,
    'saturn': 10.44,
    'earth': 9.798,
    'uranus': 8.87,
    'venus': 8.87,
    'mars': 3.71,
    'mercury': 3.7,
    'moon': 1.62,
    'pluto': 0.58}
    if body == '<earth>!':
        body_gravity = round(planet.get('earth'), 1)
        return round((mass * body_gravity), 1)
    else:
        body_gravity = round(planet.get(body), 1)
        return round((mass * body_gravity), 1)


print(force(6, 'uranus'))

def pull(m1: float, m2: float, d: float):
    return (6.674 * 10 ** -11) * ((m1 * m2) / (d ** 2))

print(pull(0.1, 5.972 * 10 ** 24, 6.371 * 10 ** 6))