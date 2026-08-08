from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    if set(drink_ingredients) & ALCOHOLS:
        return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    if dish_ingredients <= VEGAN:
        category = "VEGAN"
    elif dish_ingredients <= VEGETARIAN:
        category = "VEGETARIAN"
    elif dish_ingredients <= PALEO:
        category = "PALEO"
    elif dish_ingredients <= KETO:
        category = "KETO"
    else:
        category = "OMNIVORE"
    return f"{dish_name}: {category}"


def tag_special_ingredients(dish):
    dish_name, ingredients = dish
    return (dish_name, set(ingredients) & SPECIAL_INGREDIENTS)


def compile_ingredients(dishes):
    result = set()
    for dish in dishes:
        result |= dish
    return result


def separate_appetizers(dishes, appetizers):
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes, intersection):
    all_items = set()
    for dish in dishes:
        all_items |= dish
    return all_items - intersection