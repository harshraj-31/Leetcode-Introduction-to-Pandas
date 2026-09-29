import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers['email'] = customers['email'].str.lower()
    return customers.drop_duplicates(subset=['email'], keep='first')