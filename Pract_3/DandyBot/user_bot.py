def script(check, x, y):
    if check("level") == 1:
        if not (check("gold", x + 1, y)) and not (check("wall", x + 2, y)):
            return "right"
        elif check("gold", x + 1, y) and not (check("gold", x, y)):
            return "right"
        elif check("gold", x, y + 1) and not (check("gold", x, y)):
            return "down"
        elif check("gold", x, y):
            return "take"

    if check("level") == 2:
        if check("wall", x - 1, y):
            return "right"

        if not(check("gold", x, y)):
            return "up"

        if check("gold", x, y):
            return "take"

        if not(check("empty", x + 1, y)):
            return "right"

