# Author: Abram (Abe) Flansburg ¯\_(ツ)_/¯
# TL;DR -> *** SKIP TO THE BOTTOM FOR A FUNCTION ***

# Using Jupyter Notebook & given a dataframe "train_df" containing
# data from Ames Housing Dataset, let's profile how many NAs we have

# create an empty dictionary to store info
na_dict = {}

# loop over each col in train_df
for col in train_df:
    # get the occurences using `isnull()` and 'sum' for a total count
    na_ct = train_df[col].isnull().sum()
    if na_ct > 0:
      # if our na_ct is greater than 0
      # get the percentage of values that are Na (expressed as float)
      na_perc = round(na_ct/len(train_df), 4)
      # create a dictionary entry keyed to the column name
      # with a nested dict of count and %
      na_dict[col] = { 'count': na_ct, 'perc': na_perc }

# let's look at it now
"""
This is a clever way to sort our output.
The outer brackets {} are of course for a dict
The 'k: v for k,v in sorted(....)' begins a dictionary comprehension
within the `sorted()` function, which returns a tuple of key/value pairs,
we pass a lambda to the `key` parameter and tell it:
'sort the dict by the value (tuple index 1), but use the nested 'perc' (or you could use count)'

You can overwrite na_dict if you want:
`na_dict = {k: v for k, v in sorted(na_dict.items(), key=lambda feature: feature[1]['perc'], reverse=True)}
"""
{k: v for k, v in sorted(na_dict.items(), key=lambda feature: feature[1]['perc'], reverse=True)}

# Output:
"""
{'PoolQC': {'count': 1453, 'perc': 0.9952},
 'MiscFeature': {'count': 1406, 'perc': 0.963},
 'Alley': {'count': 1369, 'perc': 0.9377},
 'Fence': {'count': 1179, 'perc': 0.8075},
 'FireplaceQu': {'count': 690, 'perc': 0.4726},
 'LotFrontage': {'count': 259, 'perc': 0.1774},
 'GarageType': {'count': 81, 'perc': 0.0555},
 'GarageYrBlt': {'count': 81, 'perc': 0.0555},
 'GarageFinish': {'count': 81, 'perc': 0.0555},
 'GarageQual': {'count': 81, 'perc': 0.0555},
 'GarageCond': {'count': 81, 'perc': 0.0555},
 'BsmtExposure': {'count': 38, 'perc': 0.026},
 'BsmtFinType2': {'count': 38, 'perc': 0.026},
 'BsmtQual': {'count': 37, 'perc': 0.0253},
 'BsmtCond': {'count': 37, 'perc': 0.0253},
 'BsmtFinType1': {'count': 37, 'perc': 0.0253},
 'MasVnrType': {'count': 8, 'perc': 0.0055},
 'MasVnrArea': {'count': 8, 'perc': 0.0055},
 'Electrical': {'count': 1, 'perc': 0.0007}}
"""

# ------------------------------------------------------- #

# You can make this a function for easy re-use
def profile_nulls(df):
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

profile_nulls(df=train_df)