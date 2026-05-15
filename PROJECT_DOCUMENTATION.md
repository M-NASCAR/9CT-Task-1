# Assesment Task 1

#### *Purpose:* *To create a program that correctly represents if the distance a suburb is located from Sydney CBD directly effects the median house prices in that suburb.*

#### *Requirements:*
> - Data Loading - This project should have the ability to load files and handle errors such as missing files
> - Data Cleaning - This project should allow users to filter, remove and add entries to the data
> - Visulisation - This project allows for visulisation of data as graphs using matplotlib and viewing dataframes using pandas
> - Reporting - Updating data and allowing users to save
> The goal is to allow users to access,update and filter existing data through the user interface


### Hypothesis & Findings
 - My Hypothesis is that suburbs located closer to the Sydney CBD have higher median house prices
    #### My Findings:
    Suburbs located closer to the CBD usually have higher median house prices due to a wide range of factors, however the main factors are undersupply of houses, higher paying job, and a high migration rate. Sydney has significantly higher paying jobs due to global companies setting headquarters inside or near the CBD and this influx of talent and expertise significantly raises housing prices. Sydney has had a chronic problem with the undersupply of houses, this is mainly due to the high overseas immagration rate. Leading to high demand but low supply.All these factors all bring up the house prices in suburbs closer to the CBD.

 - #### Data Source:
      - [Dataframe Source, Kaggle](https://www.kaggle.com/datasets/alexlau203/sydney-house-prices)
      - [Findings Source, Propertyupdate.com](https://propertyupdate.com.au/property-investment-sydney/)


### Data Dictionary:
| Field       | Datatype  |Format for display| Description                                         | Example   | Validation                                                                       |
| :---:       |    :---   |    ---:          | :----:                                              | :----:    |      :------:                                                                    |
| price       | int       | NNNNNN           | Price of houses in dollars.                         |1120500    |Must be a number, can be any length however cannot include any decimals or strings|        
| suburb      | str       | XX...XX          | Name of the suburb in which the houses are located. |North Rocks|Must be a string, Any length and cannot include any numbers                       |
| km_from_cbd | float64   | NN.NN            | Distance from the Sydney CBD in kilometres.         |20.61      | Must be a float to two decimal places and cannot include strings                 |


