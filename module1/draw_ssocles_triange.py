def draw_isosceles_triangle(h, b):
    if b % 2 != 1 or h <= 0:
        return None

    triangle = []
    for i in range(h):
        row = [0] * b
        start = (b - 1) // 2 - i
        end = (b - 1) // 2 + i + 1
        if start < 0 or end > b:
            return None
        row[start:end] = [1] * (end - start)
        triangle.append(row)
    return triangle
print(draw_isosceles_triangle(5,11))