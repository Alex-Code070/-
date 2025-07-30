def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}

    for dish in dishes:
        if dish not in cook_book:
            print(f'Блюдо "{dish}" не найдено в кулинарной книге')
            continue

        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']

            if name in shop_list:
                shop_list[name]['quantity'] += quantity
            else:
                shop_list[name] = {'measure': measure, 'quantity': quantity}

    return shop_list
