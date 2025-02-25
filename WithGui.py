import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    api_key = "fae5b600bf42184b6140dbe551e485d8"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    city_name = city_entry.get()  # Get city name from the input field
    complete_url = f"{base_url}appid={api_key}&q={city_name}&units=metric"
    
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extract weather details
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        
        # Display the weather data
        result_label.config(text=f"Temperature: {temp}°C\nHumidity: {humidity}%\nWeather: {description.capitalize()}")
    else:
        # Show an error if the city is not found
        messagebox.showerror("Error", "City not found or API error.")

# Set up the main window
root = tk.Tk()
root.title("Weather App")

# Add a label for instructions
instruction_label = tk.Label(root, text="Enter the city name:")
instruction_label.pack(pady=10)

# Add an input field for the city name
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

# Add a button to get the weather
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

# Label to display the weather results
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
