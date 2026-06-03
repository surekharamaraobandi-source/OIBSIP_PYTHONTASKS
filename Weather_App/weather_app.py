import requests

api_key = "a11a4e7d00574cc999a85234261905"

city = input("Enter city name: ")

url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

response = requests.get(url)

data = response.json()

if "current" in data:

    city_name = data["location"]["name"]
    country = data["location"]["country"]
    temperature = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]
    condition = data["current"]["condition"]["text"]

    print("\n----- Weather Report -----")
    print("City:", city_name)
    print("Country:", country)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", condition)

else:
    print("Error:", data["error"]["message"])