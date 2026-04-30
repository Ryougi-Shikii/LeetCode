import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(inplace = True, subset = 'email')
    #print(help(customers.drop_duplicates))
    return customers