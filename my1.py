
import os

with open('recipes.txt', encoding='utf-8') as f:
    count = f.readlines().count('\n') + 1


with open('recipes.txt', encoding='utf-8') as f:
    cook_book = {}
    for i in range(count):
        dish = f.readline()[:-1]
        count_ing = int(f.readline())
        ingridients = []

        for i in range(count_ing):
            ingridient = f.readline().split(' | ')
            ing = {'ingredient_name': ingridient[0],
                   'quantity': ingridient[1],
                   'measure': ingridient[2][:-1]}
            ingridients.append(ing)
        f.readline()
        cook_book[dish] = ingridients

#print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for value in cook_book[dish]:
                if value['ingredient_name'] not in shop_list:
                    shop_list[value['ingredient_name']] = {'measure': value['measure'],
                                                           'quantity': int(value['quantity']) * person_count}
                else:
                    a = shop_list.get(value['ingredient_name'])
                    b = a['quantity']
                    shop_list[value['ingredient_name']] = {'measure': value['measure'],
                                                           'quantity': int(value['quantity']) * person_count + b}
    print(shop_list)

get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)

