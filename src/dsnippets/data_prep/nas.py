# Author: Abram (Abe) Flansburg ¯\_(ツ)_/¯
def profile_nulls(df):
    '''
    Args:
        df - input pandas dataframe
    Returns:
        Dictionary of columns with missing values sorted by percentage
        Will return 'No Nulls' if all values present
    Sample Output:
        {'PoolQC': {'count': 1453, 'perc': 0.9952},
        'MiscFeature': {'count': 1406, 'perc': 0.963},
        'FireplaceQu': {'count': 690, 'perc': 0.4726},
        'GarageYrBlt': {'count': 81, 'perc': 0.0555},
        'GarageFinish': {'count': 81, 'perc': 0.0555},
        'BsmtQual': {'count': 37, 'perc': 0.0253},
        'BsmtCond': {'count': 37, 'perc': 0.0253},
        'Electrical': {'count': 1, 'perc': 0.0007}}
    '''
    na_dict = {}
    for col in df:
        na_ct = df[col].isnull().sum()
        if na_ct > 0:
            na_perc = round(na_ct/len(df), 4)
            na_dict[col] = { 'count': na_ct, 'perc': na_perc }

    if len(na_dict.keys()) == 0:
        return 'No Nulls'
    else:
        return {k: v for k, v in sorted(na_dict.items(), key=lambda feature: feature[1]['perc'], reverse=True)}