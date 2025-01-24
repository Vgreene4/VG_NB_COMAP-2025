import pandas as pd
import numpy as np
import csv





countriesDict = pd.read_csv("countries.csv")
print(countriesDict)







# df = pd.read_csv("2025_Problem_C_Data/summerOly_athletes.csv")

# countries = df[["Team", "NOC"]].copy().drop_duplicates().sort_values(by=['NOC'], ignore_index=True)
# print(countries)
# print(countries.dtypes)




# # countries.to_csv('countries_list', index=False, header=False)

# np.set_printoptions(threshold=np.inf)
# array = countries.to_numpy()
# print(array)