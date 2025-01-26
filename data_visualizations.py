import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


medals_dtype = [('Index', int), ('Rank', int), ('Country', str), ('Gold', int), ('Silver', int), ('Bronze', int), ('Total', int), ('Year', int)]
countries = np.loadtxt("Clean Data/countries.csv", dtype=str, delimiter=",")
medals = np.loadtxt("Clean Data/summerOly_medals_counts_clean.csv", dtype=str, delimiter=",")
# print(np.delete(medals_init, 0, axis=1))
# medals = np.astype(np.delete(medals_init, 0, axis=0), medals_dtype)
# print(medals)





def graphCountry(country, medal_list):
    indiv_country = np.array([x for x in medal_list if x[2]==country])
    year, gold, silver, bronze = indiv_country.T[7].astype(int), indiv_country.T[5].astype(int), indiv_country.T[4].astype(int), indiv_country.T[3].astype(int)

    plt.bar(year, gold, color='yellow', width=2.5)
    plt.bar(year, silver, color='gray', bottom=gold, width=2.5)
    plt.bar(year, bronze, color='brown', bottom=silver+gold, width=2.5)
    plt.title(country)
    plt.xlim(1892,2028)
    plt.xticks(np.arange(1896, 2028, 4), rotation=-70)
    plt.show()


def graphYear(year, medal_list):
    indiv_year = np.array([x for x in medal_list if x[-1]==str(year)])
    print(indiv_year)

    country_list, gold, silver, bronze = indiv_year.T[2], indiv_year.T[5].astype(int), indiv_year.T[4].astype(int), indiv_year.T[3].astype(int)
    plt.bar(country_list, gold, color='yellow')
    plt.bar(country_list, silver, color='gray', bottom=gold)
    plt.bar(country_list, bronze, color='brown', bottom=silver+gold)
    plt.xticks(rotation=-90)
    plt.title(str(year))
    plt.show()


# graphYear(1900, medals)
# graphYear(1896, medals)
# graphYear(1904, medals)
# graphYear(1908, medals)

graphCountry('United States', medals)


