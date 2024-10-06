import turtle

def koch_curve(t, order, size):
    """Рекурсивна функція для побудови кривої Коха"""
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)
        t.right(120)
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)

def koch_snowflake(t, order, size):
    """Функція для побудови сніжинки Коха"""
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def main():
    # Введення рівня рекурсії
    try:
        order = int(input("Введіть рівень рекурсії (ціле число): "))
        size = 300  # Розмір сніжинки
    except ValueError:
        print("Помилка: введіть ціле число для рівня рекурсії.")
        return

    # Налаштування екрану
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Налаштування черепашки
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість

    # Початкове положення для гарної візуалізації
    t.penup()
    t.goto(-size/2, size/3)
    t.pendown()

    # Побудова сніжинки Коха
    koch_snowflake(t, order, size)

    # Завершення роботи Turtle
    turtle.done()

if __name__ == "__main__":
    main()