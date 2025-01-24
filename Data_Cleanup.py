import pandas as pd
import numpy as np


'''
Takes in the athletes file and the list of countries/NOC names we found online,
and replaces the names in the athletes file to reflect the countries list, also
sorts the athletes file first on year, and then on country. Saves the new file 
and the changes as CSV files
'''


athletes = pd.read_csv("2025_Problem_C_Data/summerOly_athletes.csv")
country_codes = pd.read_csv("countries.csv", index_col=False)

NOC_dict = dict(zip(country_codes["NOC"], country_codes["Country"]))

athletes_array = athletes.to_numpy(dtype=str)

changes_array = np.array(['Old Team Name', 'New Team Name', 'NOC'], dtype=str)

for row in athletes_array:
    if row[2] != NOC_dict[row[3]]:
        change = np.array([row[2],NOC_dict[row[3]],row[3]], dtype=str)
        changes_array = np.vstack((changes_array, change))
        row[2] = NOC_dict[row[3]]


changes_unique = np.unique(changes_array, axis=0)

athletes_df = pd.DataFrame(athletes_array)
athletes_df.columns = ["Name","Sex","Team","NOC","Year","City","Sport","Event","Medal"]

athletes_df.sort_values(by=['Year', 'NOC'], inplace=True, ignore_index=True)


print(athletes_df)

np.savetxt("name_changes.csv", changes_unique, fmt="%s", delimiter=",")
athletes_df.to_csv('summerOLY_athletes_clean.csv', index=False)