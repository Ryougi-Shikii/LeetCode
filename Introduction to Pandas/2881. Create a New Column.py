import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.insert(loc = employees.shape[1], value = employees['salary'] * 2, column = "bonus")
    return employees