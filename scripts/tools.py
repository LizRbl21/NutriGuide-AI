from query_engine import NutritionEngine

engine = NutritionEngine()

# Buscar algun alimento
def search(food):
    return engine.find_food(food)

# Comparar alimentos
def compare(food_1, food_2):
    return engine.compare_foods(
        [food_1, food_2]
    )

# Top 10 en X nutriente
def top_on(nutrient):
    return engine.top_by_nutrient(nutrient)