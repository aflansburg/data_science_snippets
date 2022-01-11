## Useful data science snippets

All of these functions can be utilized by installing and importing this repo as a package via:

```
# If using Anaconda make sure you have `git` & `pip`
conda install git pip

# make sure you're using the pip installed by conda
# otherwise you may need to update your path or
# determine correct pip from your path
which pip
# should be similar to: /Users/<user>/opt/anaconda3/bin/pip

pip install git+https://github.com/aflansburg/dsnippets
```

```
# Example usage of dsnippets.data_prep.profile_nulls in Jupyter Notebook
from dsnippets.data_prep import nas
nas.profile_nulls(some_pandas_dataframe)
```
