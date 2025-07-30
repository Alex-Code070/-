import os
from pprint import pprint

def read_cookbook(file_path: str) -> dict:
    cook_book = {}

    with open(file_path, encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break  # Конец файла

            ingredients_count = int(file.readline())
            ingredients = []

            for _ in range(ingredients_count):
                line = file.readline().strip()
                name, quantity, measure = [x.strip() for x in line.split('|')]
                ingredients.append({
                    'ingredient_name': name,
                    'quantity': int(quantity),
                    'measure': measure
                })

            cook_book[dish_name] = ingredients
            file.readline()  # Пропустить пустую строку

    return cook_book


def main():
    file_path = os.path.join(os.path.dirname(__file__), 'recipes.txt')
  # ✅ абсолютный путь
    cook_book = read_cookbook(file_path)
    pprint(cook_book)


if __name__ == '__main__':
    main()