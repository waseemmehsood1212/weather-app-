:

🌦 My Weather App

A simple and colorful Tkinter GUI application that shows real-time weather information using the WeatherAPI
.

The app allows users to enter a city name and instantly fetch temperature, humidity, and condition details in a visually pleasing interface.

✨ Features

🎨 Colorful gradient background (or fallback solid color if image missing)

🌍 Search weather by city name

🌡 Shows temperature (°C), humidity, and condition

⏩ Quick input with Enter key support

🖼 (Optional) Weather icons from WeatherAPI

🌫 (Optional) Air Quality Index (AQI) data

🛠 Requirements

Make sure you have Python 3.7+ installed, then install dependencies:

pip install requests pillow

🚀 How to Run

Clone or download this repository.

Add a background image (colorful_bg.jpg) in the same folder (optional).

Replace YOUR_API_KEY with your WeatherAPI key
.

Run the app:

python weather_app.py

📷 Screenshot

(Add your own screenshot here once you run the app)

🔑 API Key Setup

For better security, store your API key in an environment variable instead of hardcoding it:

export WEATHER_API_KEY="your_api_key_here"


And modify your code:

import os
api_key = os.getenv("WEATHER_API_KEY")

📌 Notes

The app requires an active internet connection.

WeatherAPI free tier allows 1 million calls/month with some limitations.

If no background image is found, the app falls back to a solid blue background.

📄 License

This project is for learning and personal use. Feel free to modify and enhance it. 🚀
