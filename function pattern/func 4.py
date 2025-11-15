def number_pattern(n):
    result = ""
    for i in range(1, n+1):
        for j in range(1, i+1):
            result += str(j) + " "
        result += "\n"
    return result

print(number_pattern(5))