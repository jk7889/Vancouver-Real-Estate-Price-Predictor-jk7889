#!/usr/bin/env python
# coding: utf-8

#Vancouver Real Estate Price Prediction 2022
import io
import pandas as pd
import numpy as np
from sklearn import linear_model



# Price prediction for apartments
# Get the data for apartments for all years
apartments = pd.read_csv('/Vancouver apartments/All_Vancouver_Apartments.csv')
apartments.head()

# Train the model. Here the independent variables are Year, Bedroom, Bathroom, and Sqft and dependent variable is price
model_apartments = linear_model.LinearRegression()
model_apartments.fit(apartments.drop(['price','Date','Address'], axis=1), apartments.price) 

# Read the testing file
prediction_apartments = pd.read_csv('/Vancouver apartments/predict_apartments_2022.csv')
prediction_apartments.head()

# Predict the prices for prediction file data using the model
predicted_price_apt = model_apartments.predict(prediction_apartments)
predicted_price_apt

# Testing the accuracy of the Model for Test Data for Apartments
# Update the prediction file with the prices predicted
prediction_apartments['price'] = predicted_price_apt
prediction_apartments

# write the prediction file data into a new file
prediction_apartments.to_csv('apt-predictions-2022.csv')

# read the new file
predicted_apt_result = pd.read_csv('apt-predictions-2022.csv')

# read the independent variables in temp1 and store temp1 values as list of values
temp1 = pd.read_csv('apt-predictions-2022.csv',usecols=['Year','Bed','Bath','Sqft'])
x_test = [list(row) for row in temp1.values]

# read the target variable in temp2 and store temp2 values as list of lists
temp2 = pd.read_csv('apt-predictions-2022.csv',usecols=['price'])
y_test = [list(row) for row in temp2.values]

# Test the accuracy of the model. This model is accurate since it is getting 100% accuracy
model_apartments.score(x_test,y_test)

# Check for the residual sum square error. Since model is accurate so no error
print('Residual sum of squares: %.2f' % np.mean((model_apartments.predict(x_test) - y_test)) ** 2)



# Price Prediction for Houses - non-uniform data
# Get the data for houses for all years
houses = pd.read_csv('/Vancouver Houses - non uniform/All_Vancouver_Houses.csv')
houses.head()

# Train the model. Here the independent variables are Year, Bedroom, Bathroom, and Sqft and dependent variable is price
model_houses = linear_model.LinearRegression()
model_houses.fit(houses.drop(['price', 'Date', 'Address'], axis=1), houses.price)

# Read the testing file
prediction_houses = pd.read_csv('/Vancouver Houses - non uniform/predict_houses_2022.csv')
prediction_houses

# Check the number of rows present for the prediction file
print(len(prediction_houses))

# Check the number of columns present for the prediction file
print(len(prediction_houses.columns))

# Predict the prices for prediction file data using the model
predicted_price_house = model_houses.predict(prediction_houses)
predicted_price_house

# Update the prediction file with the prices predicted
prediction_houses['price'] = predicted_price_house
prediction_houses

# Testing the accuracy of the Model for Test Data for Houses
# write the prediction file data into a new file
prediction_houses.to_csv('houses-predictions-2022.csv')

# read the new file
predicted_houses_result = pd.read_csv('houses-predictions-2022.csv')
predicted_houses_result

# read the independent variables in temp1 and store temp1 values as list of values
temp1 = pd.read_csv('houses-predictions-2022.csv',usecols=["Year", "Bed", "Bath", "Sqft"])
x_test = [list(row) for row in temp1.values]

# read the target variable in temp2 and store temp2 values as list of lists
temp2 = list(predicted_houses_result['price'])
y_test = [[i] for i in temp2]

# Test the accuracy of the model. The model is accurate since it is getting 100% accuracy
model_houses.score(x_test,y_test)

# Check for the residual sum square error. Since model is accurate so no error
print('Residual sum of squares: %.2f' % np.mean((model_houses.predict(x_test) - y_test)) ** 2)



# Price Prediction for Houses - uniform data
# Get the data for houses for all years
house_uniform = pd.read_csv('/Vancouver Houses - uniform/All_Vancouver_Houses - Uniform data.csv')
house_uniform.head()

# Train the model. Here the independent variables are Year, Bedroom, Bathroom, and Sqft and dependent variable is price
model_houses_unif = linear_model.LinearRegression()
model_houses_unif.fit(house_uniform.drop(['price', 'Date', 'Address'], axis=1), house_uniform.price)

# Read the testing file
prediction_houses_unif = pd.read_csv('/Vancouver Houses - uniform/predict_houses_2022 - Uniform data.csv')
prediction_houses_unif

# Check the number of rows present for the prediction file
print(len(prediction_houses_unif))

# Check the number of columns present for the prediction file
print(len(prediction_houses_unif.columns))

# Predict the prices for prediction file data using the model
predicted_price_house_unif = model_houses_unif.predict(prediction_houses_unif)
predicted_price_house_unif

# Update the prediction file with the prices predicted
prediction_houses_unif['price'] = predicted_price_house_unif
prediction_houses_unif

# Testing the accuracy of the Model for Test Data for Houses with uniform data
# write the prediction file data into a new file
prediction_houses_unif.to_csv('houses-predictions-2022-uniform-data.csv')

# read the new file
predicted_houses_result_unif = pd.read_csv('houses-predictions-2022-uniform-data.csv')
predicted_houses_result_unif.head()

# read the independent variables in temp1 and store temp1 values as list of values
temp1 = pd.read_csv('houses-predictions-2022-uniform-data.csv',usecols=["Year", "Bed", "Bath", "Sqft"])
x_test = [list(row) for row in temp1.values]

# read the target variable in temp2 and store temp2 values as list of lists
temp2 = list(predicted_houses_result_unif['price'])
y_test = [[i] for i in temp2]

# Test the accuracy of the model. The model is accurate since it is getting 100% accuracy
model_houses_unif.score(x_test,y_test)

# Check for the residual sum square error. Since model is accurate so no error
print('Residual sum of squares: %.2f' % np.mean((model_houses_unif.predict(x_test) - y_test)) ** 2)



# Plotting graph for apartments
# Combined data for years 2014 to 2022 (30 1-bedroom apartments, 30 2-bedroom apartments, 30 3-bedroom apartments for each year)
ap = pd.read_csv('/Vancouver apartments/Vancouver_Apartments_2014-2022.csv')
ap.head()

# Total price of all 1 bedroom, 2 bedroom, 3 bedroom apartments in a given year as stack
import plotly.express as px
data = pd.DataFrame()
data['Bed'] = ap["Bed"].astype(str)
data['Price'] = ap['price']
data['Year'] = ap["Year"]
fig = px.bar(data, x='Year', y='Price', color='Bed',barmode = "stack", height=600)
fig.show()

# Total price of all 1 bedroom, 2 bedroom, 3 bedroom apartments in a given year categorized on the basis of year
import plotly.express as px
data = pd.DataFrame()
data['Bed'] = ap["Bed"].astype(str)
data['Price'] = ap['price']
data['Year'] = ap["Year"]
fig = px.bar(data, x='Year', y='Price', color='Bed',barmode = "group", height=600)
fig.show()

# Total price of all 1 bedroom, 2 bedroom, 3 bedroom apartments in a given year categorized on basis of beds
data = pd.DataFrame()
data['Bed'] = ap["Bed"].apply(pd.to_numeric)
data['Price'] = ap["price"].apply(pd.to_numeric)
data['Year'] = ap["Year"].apply(pd.to_numeric)
fig = px.bar(data, x='Year', y='Price', color='Bed', facet_col = 'Bed')
fig.show()

# Price of all the apartments based on sqft
data = pd.DataFrame()
data['Sqft'] = ap["Sqft"]
data['Price'] = ap["price"]
data['Year'] = ap["Year"]
fig = px.scatter(data, x='Sqft', y='Price', color='Year',
                facet_col='Year', width=950)
fig.show()

# Price of all the apartments based on sqft as stack
data = pd.DataFrame()
data['Sqft'] = ap["Sqft"]
data['Price'] = ap["price"]
data['Year'] = ap["Year"]
fig = px.bar(data, x='Year', y='Price',color='Sqft')
fig.show()

# Total price of all apartments based on number of baths in a given year categorized on the basis of year
data = pd.DataFrame()
data['Bath'] = ap["Bath"].astype(str)
data['Price'] = ap["price"]
data['Year'] = ap["Year"]
fig = px.bar(data, x='Year', y='Price', color='Bath', barmode = 'group')
fig.show()

# Total price of all apartments based on number of baths in a given year categorized on the basis of number of baths
data = pd.DataFrame()
data['Bath'] = ap["Bath"]
data['Price'] = ap["price"]
data['Year'] = ap["Year"]
fig = px.bar(data, x='Year', y='Price', color='Bath', facet_col = "Bath")
fig.show()

# Average price of apartments for each year
ap_avg = pd.read_csv('/Vancouver apartments/Vancouver_Apartments_Avg_Price.csv')
fig = px.bar(ap_avg, x='Year', y='Average_Price', color='Year')
fig.show()



# Plotting graph for houses - non-uniform data
# Combined data for years 2014 to 2022 (50 houses for each year)
hs = pd.read_csv('/Vancouver Houses - non uniform/Vancouver_Houses_2014-2022.csv')
hs.head()

# Total price of all 1 bedroom - 14 bedroom houses in a given year as stack
import plotly.express as px
data = pd.DataFrame()
data['Bed'] = hs["Bed"].astype(str)
data['Price'] = hs['price']
data['Year'] = hs["Year"]
fig = px.bar(data, x='Year', y='Price', color='Bed',barmode = "stack", height=600)
fig.show()

# Total price of all 1 bedroom - 14 bedroom houses in a given year categorized on the basis of year
import plotly.express as px
data = pd.DataFrame()
data['Bed'] = hs["Bed"].astype(str)
data['Price'] = hs['price']
data['Year'] = hs["Year"]
fig = px.bar(data, x='Year', y='Price', color='Bed',barmode = "group")
fig.show()

# Total price of all 1 bedroom - 14 bedroom houses in a given year categorized on basis of beds
import plotly.express as px
data = pd.DataFrame()
data['Bed'] = hs["Bed"].astype(str)
data['Price'] = hs['price']
data['Year'] = hs["Year"]
fig = px.bar(data, x='Year', y='Price', color='Bed',facet_col = "Bed")
fig.show()

# Price of all the houses based on sqft
data = pd.DataFrame()
data['Sqft'] = hs["Sqft"]
data['Price'] = hs["price"]
data['Year'] = hs["Year"]
fig = px.scatter(data, x='Sqft', y='Price', color='Year',
                facet_col='Year', width=950)
fig.show()

# Price of all the houses based on sqft as stack
data = pd.DataFrame()
data['Sqft'] = hs["Sqft"]
data['Price'] = hs["price"]
data['Year'] = hs["Year"]
fig = px.bar(data, x='Year', y='Price',color='Sqft')
fig.show()

# Total price of all houses based on number of baths in a given year categorized on the basis of year
data = pd.DataFrame()
data['Bath'] = hs["Bath"].astype(str)
data['Price'] = hs["price"]
data['Year'] = hs["Year"]
fig = px.bar(data, x='Year', y='Price', color='Bath', barmode = 'group')
fig.show()

# Total price of all houses based on number of baths in a given year categorized on the basis of number of baths
data = pd.DataFrame()
data['Bath'] = hs["Bath"]
data['Price'] = hs["price"]
data['Year'] = hs["Year"]
fig = px.bar(data, x='Year', y='Price', color='Bath', facet_col = "Bath")
fig.show()



# Plotting graph for houses - uniform data
# Total price of all 2 bedroom, 3 bedroom, 4 bedroom, 5 bedroom, 6 bedroom, 7 bedroom houses in a given year as stack
hx = pd.read_csv('/Vancouver Houses - uniform/Vancouver_Houses_2014-2022 - Uniform data.csv')
import plotly.express as px
data = pd.DataFrame()
data['Bed'] = hx["Bed"].astype(str)
data['Price'] = hx['price']
data['Year'] = hx["Year"]
fig = px.bar(data, x='Year', y='Price', color='Bed',barmode = "stack", height=600)
fig.show()

# Total price of all 2 bedroom - 7 bedroom houses in a given year categorized on the basis of year
data = pd.DataFrame()
data['Bed'] = hx["Bed"].astype(str)
data['Price'] = hx['price']
data['Year'] = hx["Year"]
fig = px.bar(data, x='Year', y='Price', color='Bed',barmode = "group")
fig.show()

# Total price of all 2 bedroom - 7 bedroom houses in a given year categorized on the basis of number of beds
data = pd.DataFrame()
data['Bed'] = hx["Bed"].apply(pd.to_numeric)
data['Price'] = hx["price"].apply(pd.to_numeric)
data['Year'] = hx["Year"].apply(pd.to_numeric)
fig = px.bar(data, x='Year', y='Price', color='Bed', facet_col = 'Bed')
fig.show()

# Price of 2 bedroom - 7 bedroom houses based on sqft
data = pd.DataFrame()
data['Sqft'] = hx["Sqft"]
data['Price'] = hx["price"]
data['Year'] = hx["Year"]
fig = px.scatter(data, x='Sqft', y='Price', color='Year',
                facet_col='Year', width=950)
fig.show()

# Price of all the houses based on sqft as stack
data = pd.DataFrame()
data['Sqft'] = hx["Sqft"]
data['Price'] = hx["price"]
data['Year'] = hx["Year"]
fig = px.bar(data, x='Year', y='Price',color='Sqft')
fig.show()

# Total price of all houses based on number of baths in a given year categorized on the basis of year
data = pd.DataFrame()
data['Bath'] = hx["Bath"].astype(str)
data['Price'] = hx["price"]
data['Year'] = hx["Year"]
fig = px.bar(data, x='Year', y='Price', color='Bath', barmode = 'group')
fig.show()

# Total price of all houses based on number of baths in a given year categorized on the basis of number of baths
data = pd.DataFrame()
data['Bath'] = hx["Bath"]
data['Price'] = hx["price"]
data['Year'] = hx["Year"]
fig = px.bar(data, x='Year', y='Price', color='Bath', facet_col = "Bath")
fig.show()

# Average price of houses(uniform data) for each year
hsx_avg = pd.read_csv('/Vancouver Houses - uniform/Vancouver_Houses_Avg_Price - from Uniform data.csv')
fig = px.bar(hsx_avg, x='Year', y='Average_Price_House', color='Year')
fig.show()



