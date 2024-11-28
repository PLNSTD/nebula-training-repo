import requests

OWAPI_key = 'adf0ea1edcd4b4cecfcebca30aaadf58'
city_name = input('Type the city of which you want the wather... ')

city_id = '4098776'
OpenWeatherURL = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OWAPI_key}'
 
response = requests.get(OpenWeatherURL)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    weather_info = data['weather'][0]
    city_temp = data['main']['temp']
    print(f"Main Weather: {weather_info['main']}")
    print(f"Description: {weather_info['description']}")
    print(f"Temperature: {city_temp}")
else:
    print(f'Failed to retrieve data. Status code: {response.status_code}')