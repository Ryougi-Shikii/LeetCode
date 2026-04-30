import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # print(help(students.isnull))
    return students[students['name'].notnull()]