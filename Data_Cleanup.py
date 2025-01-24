import pandas as pd


df = pd.read_csv("2025_Problem_C_Data/summerOly_athletes.csv")

countries = df[["Team", "NOC"]].copy().drop_duplicates().sort_values(by=['NOC'], ignore_index=True)
print(countries)
print(countries.dtypes)




# countries.to_csv('countries_list', index=False, header=False)


# array = countries.to_numpy()
# print(array)