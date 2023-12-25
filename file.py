def triangle_pattern(n):
    for i in range(1, n + 1):
        print('* ' * i)
#example usage
triangle_pattern(5)

def square_pattern(n):
    for i in range(n):
        print('* ' * n)
square_pattern(4)

def right_angle_triangle(n):
    for i in range(1, n + 1):
        spaces = " " * (n-i)
        stars = '*' * i
        print(spaces + stars)

right_angle_triangle(5)

def diamond_pattern(n):
    # upper part of the diamond
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

    # lower part of the diamond
    for i in range(n - 1, 0, -1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

diamond_pattern(5)



    