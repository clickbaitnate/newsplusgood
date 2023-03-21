import requests

# Get your API key from the NewsAPI website (https://newsapi.org/)
API_KEY = "Insert your API key here"

# Set the parameters for the API request
params = {
    "apiKey": API_KEY,
    "country": "us",
}

# Make the API request to get the top headlines
response = requests.get("https://newsapi.org/v2/top-headlines", params=params)

# Ask the user for their zip code
zip_code = input("Enter your zip code: ")

# Check the status code of the response to make sure the request was successful
if response.status_code == 200:
    # If the request was successful, parse the response data
    data = response.json()
    articles = data["articles"]

    # Print the top headlines and links to the articles to the CLI, coloring the headlines and links differently
    print("\033[1mTop News Headlines of the Day:\033[0m")  # Bold font for the heading
    for i, article in enumerate(articles):
        # Color the headline yellow and the link blue
        print("\033[93m{}. {}\033[0m".format(i+1, article["title"]))
        print("   \033[94mLink: {}\033[0m".format(article["url"]))
else:
    # If the request was unsuccessful, print an error message
    print("An error occurred while fetching the news headlines. Please try again later.")



# Use the OpenWeatherMap API to get the weather data for the user's zip code
API_KEY = "362280e5c01435445d0955acbbae8e5e"
api_url = "https://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}".format(zip_code, API_KEY)
response = requests.get(api_url)
weather_data = response.json()

# Extract the relevant weather data from the API response
temperature = weather_data['main']['temp']
chance_of_rain = weather_data['weather'][0]['description']
feels_like = weather_data['main']['feels_like']

# Use the "feels like" temperature to suggest appropriate clothing
if feels_like > 80:
    clothing_suggestion = "It's hot out, you might want to wear shorts and a t-shirt 🌞"
elif feels_like > 60:
    clothing_suggestion = "It's mild out, you might want to wear a light jacket or sweater 🌼"
elif feels_like > 40:
    clothing_suggestion = "It's cool out, you might want to wear a coat or a heavier sweater 🍂"
else:
    clothing_suggestion = "It's cold out, you might want to wear a heavy coat and gloves ❄️"

# Print the weather data and clothing suggestion to the CLI
print("Temperature: {}°F {}".format(temperature, "🌡️"))
print("Chance of rain: {} {}".format(chance_of_rain, "🌧️"))
print("Feels like: {}°F {}".format(feels_like, "🌡️"))
print(clothing_suggestion)
