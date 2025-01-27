import numpy as np
import pandas as pd

'''
for country, year
- get data from programs
- get data from medals
- get data from athletes
- get data from hosts


export data as a numpy binary in the form
[[x1,y1],
[x2,y2],
...
[xn,yn]]

where 
xi = [
    NOC, 
    year, 
    #athletes, 
    host
    #events, 
    #sports, 
    #disciplines, 
]
and
yi = [
    # golds
    # silvers
    # bronzes
    # total
]

A data point only exists IF a team competed that year, otherwise there is none.

'''

NOC_num_dict = {'AFG': 0,'AHO': 1,'ALB': 2,'ALG': 3,'AND': 4,'ANG': 5,'ANT': 6,'ARG': 7,'ARM': 8,'ARU': 9,'ASA': 10,'AUS': 11,'AUT': 12,'AZE': 13,'BAH': 14,'BAN': 15,'BAR': 16,'BDI': 17,'BEL': 18,'BEN': 19,'BER': 20,'BHU': 21,'BIH': 22,'BIZ': 23,'BLR': 24,'BOL': 25,'BOT': 26,'BRA': 27,'BRN': 28,'BRU': 29,'BUL': 30,'BUR': 31,'CAF': 32,'CAM': 33,'CAN': 34,'CAY': 35,'CGO': 36,'CHA': 37,'CHI': 38,'CHN': 39,'CIV': 40,'CMR': 41,'COD': 42,'COK': 43,'COL': 44,'COM': 45,'CPV': 46,'CRC': 47,'CRO': 48,'CUB': 49,'CYP': 50,'CZE': 51,'DEN': 52,'DJI': 53,'DMA': 54,'DOM': 55,'ECU': 56,'EGY': 57,'EOR': 58,'ERI': 59,'ESA': 60,'ESP': 61,'EST': 62,'ETH': 63,'FIJ': 64,'FIN': 65,'FRA': 66,'FRG': 67,'FSM': 68,'GAB': 69,'GAM': 70,'GBR': 71,'GBS': 72,'GDR': 73,'GEO': 74,'GEQ': 75,'GER': 76,'GHA': 77,'GRE': 78,'GRN': 79,'GUA': 80,'GUI': 81,'GUM': 82,'GUY': 83,'HAI': 84,'HKG': 85,'HON': 86,'HUN': 87,'INA': 88,'IND': 89,'IOA': 90,'IRI': 91,'IRL': 92,'IRQ': 93,'ISL': 94,'ISR': 95,'ISV': 96,'ITA': 97,'IVB': 98,'JAM': 99,'JOR': 100,'JPN': 101,'KAZ': 102,'KEN': 103,'KGZ': 104,'KIR': 105,'KOR': 106,'KOS': 107,'KSA': 108,'KUW': 109,'LAO': 110,'LAT': 111,'LBA': 112,'LBN': 113,'LBR': 114,'LCA': 115,'LES': 116,'LIE': 117,'LTU': 118,'LUX': 119,'MAD': 120,'MAL': 121,'MAR': 122,'MAS': 123,'MAW': 124,'MDA': 125,'MDV': 126,'MEX': 127,'MGL': 128,'MHL': 129,'MKD': 130,'MLI': 131,'MLT': 132,'MNE': 133,'MON': 134,'MOZ': 135,'MRI': 136,'MTN': 137,'MYA': 138,'NAM': 139,'NCA': 140,'NED': 141,'NEP': 142,'NGR': 143,'NIG': 144,'NOR': 145,'NRU': 146,'NZL': 147,'OMA': 148,'PAK': 149,'PAN': 150,'PAR': 151,'PER': 152,'PHI': 153,'PLE': 154,'PLW': 155,'PNG': 156,'POL': 157,'POR': 158,'PRK': 159,'PUR': 160,'QAT': 161,'ROU': 162,'RSA': 163,'RUS': 164,'RWA': 165,'SAM': 166,'SCG': 167,'SEN': 168,'SEY': 169,'SGP': 170,'SKN': 171,'SLE': 172,'SLO': 173,'SMR': 174,'SOL': 175,'SOM': 176,'SRB': 177,'SRI': 178,'SSD': 179,'STP': 180,'SUD': 181,'SUI': 182,'SUR': 183,'SVK': 184,'SWE': 185,'SWZ': 186,'SYR': 187,'TAN': 188,'TCH': 189,'TGA': 190,'THA': 191,'TJK': 192,'TKM': 193,'TLS': 194,'TOG': 195,'TPE': 196,'TTO': 197,'TUN': 198,'TUR': 199,'TUV': 200,'UAE': 201,'UGA': 202,'UKR': 203,'URS': 204,'URU': 205,'USA': 206,'UZB': 207,'VAN': 208,'VEN': 209,'VIE': 210,'VIN': 211,'VNM': 212,'YAR': 213,'YEM': 214,'YUG': 215,'ZAM': 216,'ZIM': 217}

athlete_df = pd.read_csv('Clean Data/summerOly_athletes_cropped.csv', usecols=[0,3,4])
athlete_list = athlete_df.to_numpy(dtype=str)
country_list = np.loadtxt('Clean Data/summerOly_countries_cropped.csv', delimiter=",", dtype=str)
medal_counts = np.loadtxt('Clean Data/summerOly_medals_clean.csv', delimiter=",", dtype=str, skiprows=1, usecols=[3,4,5,6,7,8])
host_list = np.loadtxt('Clean Data/summerOly_hosts_clean.csv', delimiter=',', dtype=str, skiprows=1, usecols=[0,2])
programs_list = np.loadtxt('Clean Data/summerOly_programs_cropped.csv', delimiter=',', dtype=str)

competed_arr, num_athletes = np.unique(athlete_list[:,1:], axis=0, return_counts=True)


x_data = np.empty(shape=(3084,8), dtype=int)
y_data = np.empty(shape=(3084,5), dtype=int)

for index,row in enumerate(competed_arr):
    year, country = row[1], str(row[0])
    
    amt_athletes = int(num_athletes[index])
    # host country
    for hosts in host_list:
        if hosts[0] == year:
            host = str(hosts[1])

    # get events/disciplines/sports
    for e in programs_list.T:
        if e[0] == year:
            programs = e[1:]
            events = int(programs[0])
            disciplines = int(programs[1])
            sport = int(programs[2])

    # get medal counts, in the form G/S/B/Total
    score = [0,0,0,0]
    for e in medal_counts:
        if e[4] == year and e[5] == country:
            score = e[0:4].astype(int)

    x = np.array([index, NOC_num_dict[country], int(year), amt_athletes, NOC_num_dict[host], events, disciplines, sport], dtype=int)
    y = np.array(np.append(index, score), dtype=int)

    x_data[index] = x
    y_data[index] = y


np.savez('Training Data/pre_medals_data', x_data=x_data, y_data=y_data )