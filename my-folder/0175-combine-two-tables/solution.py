import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    resultDf = person.merge(address, how='left', on = 'personId')
    return resultDf[['firstName', 'lastName', 'city', 'state']]
