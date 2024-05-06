def print_table(data):
    # Визначаємо максимальну ширину кожного стовпчика
    max_lengths = [max(len(str(value)) for value in column) for column in zip(*data)]

    # Виводимо верхню лінію таблиці
    print("+" + "+".join("-" * (length + 2) for length in max_lengths) + "+")

    # Виводимо дані
    for row in data:
        print("| " + " | ".join(str(value).ljust(length) for value, length in zip(row, max_lengths)) + " |")

    # Виводимо нижню лінію таблиці
    print("+" + "+".join("-" * (length + 2) for length in max_lengths) + "+")

# Приклад використання
data = [
    ("Рівень логування", "Кількість"),
    ("INFO", 4),
    ("DEBUG", 3),
    ("ERROR", 2),
    ("WARNING", 1)
]

print_table(data)