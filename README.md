# Vancouver Real Estate Price Predictor

* Predicts prices for different housing options in Vancouver for 2022 by analysing the data of the previous 7 years (2014 - 2021)
* Compares the effects of different factors that is number of bedrooms, number of bathrooms, area (sqft) and average price of different housing options in Vancouver such as apartments and houses on the future market value of real estate in Vancouver
* Creates a training model and tests the accuracy of the prediction by using Linear Regression Algorithm

# Libraries/Technologies implemented

> **Jupyter notebook and Python 3** – Jupyter Notebook has been used to write the source code for the project and represent data in Python language. 

>  <p align="justify"> <b>Pandas</b> – It has been used in this project to read, store and manipulate data from All_Vancouver_Apartments.csv and All_Vancouver_Houses.csv files. Both files contain data from years 2014 to 2021 and has been used to predict prices for 1 bedroom, 2 bedroom, 3 bedroom apartments and 1-14 bedroom houses (non-uniform data) and 2-7 bedroom houses (uniform-data) in 2022. <p>

> **Plotly** – plotly.express is a built-in module in plotly library in Python which is used for creating and representing data in figures like graphs, charts, diagrams and maps (basically data visualisation). It has been used in this project to show two things:-

* **Bar graphs** which represent relationship between number of bedrooms, area(sqft) and number of bathrooms with price for apartments and houses                   in Vancouver for years 2014 to 2021.
* **Scatter graphs** representing relationship between square feet (sqft) and price for apartments and houses in Vancouver for years 2014 to 2021.

# Dataset used in the project

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

# Files in this project
There are 11 files in this project
