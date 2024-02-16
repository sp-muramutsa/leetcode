import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype(np.uint8, copy=False)

    return students
    
