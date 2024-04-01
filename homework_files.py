def read_recipes(file: str) -> dict:
    cook_book = {}
    with open(file, encoding="utf-8") as f:
        for line in f:
            dish = line.strip()
            ingredients_count = int(f.readline().strip())
            ingredients = []
            for i in range(ingredients_count):
                ingredient_name, quantity, measure = f.readline().strip().split(" | ")
                ingredients.append({
                    "ingredient_name": ingredient_name,
                    "quantity": quantity,
                    "measure": measure
                })
            cook_book[dish] = ingredients
            f.readline()
    return cook_book


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    cook_book = read_recipes("recipes.txt")
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = ingredient["ingredient_name"]
            if new_shop_list_item not in shop_list:
                shop_list[new_shop_list_item] = {"measure": ingredient["measure"]}
                shop_list[new_shop_list_item]["quantity"] = int(ingredient["quantity"]) * person_count
            else:
                shop_list[new_shop_list_item]["quantity"] += int(ingredient["quantity"]) * person_count
    return shop_list


cook_book = read_recipes("recipes.txt")
print(cook_book)
shop_list = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 5)
print(shop_list)
