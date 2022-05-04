# Vancouver Real Estate Price Predictor

* **Predicts prices** for different housing options in Vancouver for 2022 by analysing the data of the previous 7 years (2014 - 2021)
* **Compares the effects of different factors** that is number of bedrooms, number of bathrooms, area (sqft) and average price of different housing options in Vancouver such as apartments and houses on the future market value of real estate in Vancouver
* **Creates a training model** and **tests the accuracy** of the prediction by using Linear Regression Algorithm

# Libraries/Technologies implemented

> **Jupyter notebook and Python 3** – Jupyter Notebook has been used to write the source code for the project and represent data in Python language. 

>  <p align="justify"> <b>Pandas</b> – It has been used in this project to read, store and manipulate data from All_Vancouver_Apartments.csv and All_Vancouver_Houses.csv files. Both files contain data from years 2014 to 2021 and has been used to predict prices for 1 bedroom, 2 bedroom, 3 bedroom apartments and 1-14 bedroom houses (non-uniform data) and 2-7 bedroom houses (uniform-data) in 2022. <p>

> **Plotly** – plotly.express is a built-in module in plotly library in Python which is used for creating and representing data in figures like graphs, charts, diagrams and maps (basically data visualisation). It has been used in this project to show two things:-

* **Bar graphs** which represent relationship between number of bedrooms, area(sqft) and number of bathrooms with price for apartments and houses                   in Vancouver for years 2014 to 2021.
* **Scatter graphs** representing relationship between square feet (sqft) and price for apartments and houses in Vancouver for years 2014 to 2021.

# Sources for gathered data
  
> Wayback machine (https://archive.org/web/) is a tool on the internet where we can put URL of any web page to find its history i.e. snapshots of what it looked like in previous years.

> Data for apartments and house prices in Vancouver 2014 to 2021 has been gathered by putting the below URLs in this site and finding real time snapshots of prices back in 2014, 2015, 2016, 2017, 2018, 2019, 2020 and 2021 

> From this data All_Vancouver_Apartments.csv  and All_Vancouver_Houses.csv has been created. The URLs used for gathering data are:-

* https://www.point2homes.com/CA/Real-Estate-Listings/BC/Vancouver.html
* https://www.zolo.ca/vancouver-real-estate
* https://www.condoinvancouver.ca/solds.html
* https://www.condoinvancouver.ca/properties.html
* https://www.condoinvancouver.ca/mls_3-bed-downtown.html
* https://www.rew.ca/properties/areas/vancouver-bc/type/apartment-condo
* https://www.rew.ca/properties/areas/vancouver-bc
* https://www.remax.ca/bc/vancouver-real-estate
* https://vancouvertownhouse.ca/townhouse/3-bedroom/
* https://www.mikegrahame.com/vancouver-luxury-condos
* https://www.zillow.com/downtown-vancouver-bc/
* https://www.zillow.com/vancouver-bc/
* https://www.northshorerealty.ca/north-vancouver-condos.php
* https://www.myvancouverproperty.ca/houses-for-sale-in-vancouver-3000000
* https://www.zoocasa.com/vancouver-bc-real-estate
* https://www.westsiderealty.ca/Properties.php
* https://www.realtor.ca/bc/vancouver/real-estate
* https://www.realtor.ca/bc/vancouver/downtown/real-estate
* https://vancouvercanadahomes.com/buying/real-estate-listings/kitsilano/houses
* https://vancouvertownhouse.ca/featured-listings/
* https://www.royallepage.ca/en/bc/vancouver/properties/
* https://www.vancouverforsale.ca/vancouver-mls-listings/

# Algorithm Implemented
Linear Regression

# Data for this project
There are `11 csv files` in this project
  
## Files in Vancouver apartments
  *  <p align="justify"><b>All_Vancouver_Apartments.csv</b> - This file contains information regarding <code>90 Vancouver apartments</code> further divided into 30 1 bedroom apartments, 30 2 bedroom apartments and 30 3 bedroom apartments for each year from 2014-2021. This file is used as the training model for Vancouver apartment price prediction for 2022.</p>
  
* **pedict_apartments_2022.csv** - This file contains values such as `number_of_bedrooms`, `number_of_bathrooms` and `area in sqft` for Vancover apartments in 2022 whose price is predicted based on the Vancouver apartments training model
  
* <p align="justify"><b>Vancouver_Apartments_2014-2022.csv</b> - A compilation of 2 files:- All_Vancouver_Apartments.csv and predict_apartments_2022.csv. It consists of values for all Vancouver Apartments including the predicted prices and values for apartments in 2022. The use of this csv is for comparison purposes. </p>
  
* **Vancouver_Apartments_Avg_Price.csv** - This file contains `average price` of 90 apartments for each year (2014 - 2022). The use of this csv is for comapring average price over the years.
  
## Files in Vancouver Houses - non uniform
* <p align="justify"><b>All_Vancover_Houses.csv</b> -  This file contains information regarding <code> 50 Vancouver houses </code> ranging from 1 bedoom to 14 bedroom for years 2014-2021. This file is used as the training model for Vancouver house price prediction for 2022. This file contains non-uniform data which means two distinct years don't have equal houses with same number of bedrooms. Eg. Year 2014 has only one 1 bedroom house, Year 2015 has three 1 bedroom houses and Year 2016 has zero 1 bedroom houses. </p>
  
* <p align="justify"><b>predict_houses_2022.csv</b> - This file contains values such as <code>number_of_bedrooms</code>, <code>number_of_bathrooms</code> and <code>area in sqft</code> for Vancover Houses in 2022 whose price is predicted based on the Vancouver houses training model for non uniform data.</p>
  
* <p align="justify"><b>Vancouver_Houses_2014-2022.csv</b> - This file is a compilation of 2 files:- All_Vancouver_Houses.csv and predict_houses_2022.csv. It consists of values for all Vancouver Houses including the predicted prices and values for houses in 2022 for non uniform data. The use of this csv is for comparison purposes.</p>
  
 ## Files in Vancouver Houses - uniform
 *  <p align="justify"><b>All_Vancouver_Houses - Uniform data.csv</b> - This file contains uniform data regarding <code>60 Vancouver houses</code> further divided into 10 2 bedroom houses, 10 3 bedroom houses, 10 4 bedroom houses, 10 5 bed</b>room houses, 10 6 bedroom houses and 10 7 bedroom houses for each year from 2014-2021. This file is used as the training model for Vancouver house price prediction (with uniform data) for 2022.</p>
  
 *  <p align="justify"><b>predict_houses_2022 - Uniform data.csv</b> - This file This file contains values such as <code>number_of_bedrooms</code>,<code> number_of_bathrooms</code> and <code>area in sqft</code> for Vancover Houses in 2022 whose price is predicted based on the Vancouver houses training model for uniform data.</p>
  
 * <p align="justify"> <b>Vancouver_Houses_2014-2022 - Uniform data.csv</b> - This file is a compilation of 2 files:- All_Vancouver_Houses - Uniform data.csv and predict_houses_2022 - Uniform data.csv. It consists of values for all Vancouver Houses including the predicted prices and values for houses in 2022 for uniform data. The use of this csv is for comparison purposes.</p>
  
 * **Vancouver_Houses_Avg_Price - from Uniform data.csv** - This file contains <code>average price</code> of 60 houses for each year (2014 - 2022). The use of this csv is for comapring average price over the years.
  
