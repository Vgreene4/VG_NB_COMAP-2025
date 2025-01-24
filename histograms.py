import pandas as pd
import numpy as np
import seaborn as sns


countries = pd.read_csv("Clean Data/countries.csv", dtype=str, delimiter=",")
medals = pd.read_csv("Clean Data/summerOly_medals_counts_clean.csv", delimiter=",", dtype=str, index_col=False)


print(countries)
print(medals)