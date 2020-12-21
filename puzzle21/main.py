import sys

class food:
    def __init__(self, ingredients, allergenes):
        self.ingredients = ingredients
        self.allergenes = allergenes

    def __repr__(self):
        return "{} (contains {})".format("|".join(self.ingredients), "|".join(self.allergenes))

foods = []
for line in sys.stdin.readlines():
    allergene_idx = line.index(" (")
    ingredients = line[:allergene_idx].split(" ")
    allergenes = line[allergene_idx+2+len("contains "):line.index(")")].split(", ")
    foods.append(food(ingredients, allergenes))

print("Parsed: {}".format(foods))
all_ingredients = [i for f in foods for i in f.ingredients]
print("all: {}".format(all_ingredients))
for food in foods:
    for allergene in food.allergenes:
        for check_food in foods:
            if check_food == food:
                continue
            if allergene in check_food.allergenes:
                for ingredient in food.ingredients:
                    if ingredient in check_food.ingredients:
                        all_ingredients = list(filter(lambda i: ingredient != i, all_ingredients))

print("filtered: {} {}".format(all_ingredients, len(all_ingredients)))
