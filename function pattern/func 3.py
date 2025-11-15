def get_pattern():
    pattern = ""
    for i in range(1, 6):
        pattern += " " * (5 - i) + "*" * (2*i - 1) + "\n"
    return pattern

print(get_pattern())
