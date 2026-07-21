from load_data import load_dataset

class NutritionEngine:

    def __init__(self):
        self.df = load_dataset()

    # Busqueda de Alimentos
    def find_food(self, food_name):
        result = self.df[self.df["Food"].str.contains(food_name, case=False, na=False)]
        return result
    
    # Hacer comparaciones
    def compare_foods(self, foods):
        result = self.df[self.df["Food"].isin(foods)]
        return result
    
    # Rankear alimentos, 10 mejores
    def top_by_nutrient(self, nutrient, top_n=10):
        return (
            self.df
            .sort_values(
                by=nutrient,
                ascending=False
            )
            .head(top_n)
        )
    
    # Filtro general
    def filter_foods(
        self,
        protein=None,
        calories=None,
        fiber=None,
        sugar=None,
        cholesterol=None,
        sodium=None,
        fat=None):

        df = self.df.copy()

        if protein is not None:
            df = df[
                df["Protein"] >= protein
            ]

        if calories is not None:
            df = df[
                df["Caloric Value"] <= calories
            ]

        if fiber is not None:
            df = df[
                df["Dietary Fiber"] >= fiber
            ]

        if sugar is not None:
            df = df[
                df["Sugars"] <= sugar
            ]
        
        if cholesterol is not None:
            df = df[
                df["Cholesterol"] <= cholesterol
            ]
        
        if sodium is not None:
            df = df[
                df["Sodium"] <= sodium
            ]
        
        if fat is not None:
            df = df[
                df["Fat"] <= fat
            ]

        return df
    
    # Filtros por valores
    ## Calorias
    def calories_less_than(self, calories):
        return self.df[
            self.df["Caloric Value"] <= calories
        ]
    
    ## Grasas
    def fats_less_than(self, fats):
        return self.df[
            self.df["Fat"] <= fats
        ]
    
    ## Carbohidratos
    def carbohydrates_less_than(self, carbs):
        return self.df[
            self.df["Carbohydrates"] <= carbs
        ]
    
    ## Azucar
    def sugars_less_than(self, sugars):
        return self.df[
            self.df["Sugars"] <= sugars
        ]
    
    ## Sodio
    def sodium_less_than(self, sodium):
        return self.df[
            self.df["Sodium"] <= sodium
        ]

    ## Colesterol
    def cholesterol_less_than(self, chol):
        return self.df[
            self.df["Cholesterol"] <= chol
        ]
    
    ## Protein
    def protein_more_than(self, protein):
        return self.df[
            self.df["Protein"] >= protein
        ]
    
    ## Fibra
    def fiber_more_than(self, fiber):
        return self.df[
            self.df["Dietary Fiber"] >= fiber
        ]