import requests,json
Api_key="fae5b600bf42184b6140dbe551e485d8"
base_url="http://api.openweathermap.org/data/2.5/weather?"
city_name=input("Enter your city : ")
complete_url=f"{base_url}appid={Api_key}&q={city_name}&units=metric"
response = requests.get(complete_url)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print("Current Weather:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print("Failed to retrieve weather data")
