import pandas as pd
import numpy as np
import seaborn as sns

countries = pd.read_csv("countries.csv", dtype=str)[1]

print(countries)