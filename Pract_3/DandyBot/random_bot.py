import random


def script(check, x, y):
    if not(check("gold", x, y)):
        return "up"
    return random.choice(["pass", "left", "right", "up", "down"])
