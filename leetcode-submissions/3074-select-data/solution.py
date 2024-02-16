import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    target_student = students[students["student_id"] == 101]

    return target_student[["name", "age"]]

   
    
