predict_medals_data.npz has two numpy arrays, accessible with keywords 'x_data'
and 'y_data'. The x data has the order [index, NOC, year, amt_athletes, host, 
events, disciplines, sport], and the y data has the order [index, gold, silver,
bronze, total]. The index is just for reference, and to make sure the right data
pairs are associated. Drop them before training the model.

Load the data with 'data = np.load(path_to_data)', and 'x = data['x_data']' 
gives the x data. The same for the y data.