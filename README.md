
# Weather_displaying_DA_Batch1 


# Intro:
I made this project  as apart of training of python programming in Aiapproach club.

# Objective

1- Apply programming concepts: The app utilizes Python programming principles (API,loop, OOP etc.)  learned in the AI approach club course to structure the code and enhance its functionality.

2-Get weather data: The app uses the Open Weather API to retrieve weather information for a specific city.

3- Show weather in different ways: The app presents weather data in text, tables, and graphs for easy understanding. This includes current weather, 24-hour forecast, and a 5-day forecast.

4- Being easy to use: The app is simple for users to input their city and get the weather information they need.

# About the dataset

This Weather Forecast Application utilizes data from the OpenWeatherMap API, a widely recognized source for weather information. The API provides a range of weather-related data, including:

1- Current Weather Data: This includes current temperature, feels-like temperature, minimum and maximum temperatures, humidity, atmospheric pressure, wind speed, wind direction, cloudiness, and weather condition description.

2- 5-Day Forecast Data: This dataset provides weather forecasts for the next 5 days at 3-hour intervals. It includes similar parameters as the current weather data but projected for future time periods.

# Steps :

1- Import necessary libraries: Begin by importing the required libraries, including requests for making API calls, pandas for data manipulation, and matplotlib for visualization.

2- Define classes: Create classes to represent different aspects of the application's functionality, such as Current_Weather, Weather_Forecast, numerical_Weather_Data, text_Weather_Data, Plot_TheForecast_Over24h, and Show_5Days_Forecasting. These classes encapsulate data retrieval, processing, and presentation logic.

3- Implement API integration: Define functions (current_weather_api and forecast_weather_api) to interact with the OpenWeatherMap API. These functions handle API requests, data parsing, and error management.

4- Get user input: Prompt the user to enter the city name for which they want to retrieve weather information.

5- Fetch weather data: Use the API integration functions to fetch current and forecast data for the specified city.

6- Process data: Utilize the defined classes and their methods to process and analyze the weather data. This includes converting temperatures, extracting relevant parameters, and organizing data into data structures.

7- Present data: Depending on user choices, present the weather data in various formats. This involves calling methods of the respective classes to generate textual reports, numerical tables, and graphical visualizations.

8- Handle errors: Implement error handling mechanisms to gracefully manage potential issues like invalid city names or API request failures.

9- Organize code: Structure the code logically using classes, functions, and comments to ensure readability and maintainability.

10- Test and refine: Thoroughly test the application's functionality with different inputs and scenarios. Make necessary adjustments and refinements to improve accuracy and user experience.

# Conclusion of project:

This project successfully delivered a functional Weather Forecast Application leveraging the OpenWeatherMap API and object-oriented programming principles. Users can access current weather, 24-hour forecasts, and 5-day outlooks in user-friendly formats. By integrating Python libraries and incorporating error handling, the application provides robust and informative weather data. This project demonstrates practical programming skills applied to a real-world scenario.


