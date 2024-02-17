import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    animals.sort_values("weight", ascending=False, inplace=True)
    heavy_animals = animals[animals["weight"] > 100]

    return pd.DataFrame(heavy_animals["name"])

    
