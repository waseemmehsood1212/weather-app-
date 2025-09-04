import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow

# --- Function to get weather data ---
def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name!")
        return

    api_key = "cf117aa87a6348c0b9c164905250209"  # ✅ Your WeatherAPI key
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        # Check for errors
        if "error" in data:
            messagebox.showerror("Error", data["error"]["message"])
            return

        # Extract data
        city_name = data["location"]["name"]
        country = data["location"]["country"]
        temp = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        desc = data["current"]["condition"]["text"]

        result_label.config(
            text=f"📍 {city_name}, {country}\n\n"
                 f"🌡 Temperature: {temp} °C\n"
                 f"💧 Humidity: {humidity}%\n"
                 f"☁ Condition: {desc}"
        )

    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve data: {e}")


# --- Tkinter UI setup ---
root = tk.Tk()
root.title("My Weather App")
root.geometry("650x550")
root.resizable(False, False)

# --- Load Colorful Gradient Background ---
try:
    bg_image = Image.open("colorful_bg.jpg")  # 🖼 Use any colorful gradient image
    bg_image = bg_image.resize((650, 550), Image.ANTIALIAS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception:
    root.config(bg="#74b9ff")  # fallback blue background

# Title
title_label = tk.Label(
    root, 
    text="🌈 My Weather App 🌦", 
    font=("Comic Sans MS", 26, "bold"), 
    bg="#000000", fg="white",
    padx=15, pady=5
)
title_label.pack(pady=15)

# Input frame (semi-transparent look)
input_frame = tk.Frame(root, bg="#ffffff", bd=3, relief="ridge")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Enter city name:", font=("Arial", 14, "bold"), bg="white", fg="#2c3e50").grid(row=0, column=0, padx=10, pady=10)

city_entry = tk.Entry(input_frame, font=("Arial", 14), justify="center", width=20, bd=2, relief="groove", fg="#2c3e50")
city_entry.grid(row=0, column=1, padx=10, pady=10)

# Search button (colorful style)
search_btn = tk.Button(
    root, 
    text="☀ Get Weather ☔", 
    font=("Arial", 14, "bold"), 
    bg="#ff7675", fg="white",
    activebackground="#d63031", activeforeground="white",
    relief="flat", padx=25, pady=10,
    command=get_weather
)
search_btn.pack(pady=15)

# Result frame (styled card)
result_frame = tk.Frame(root, bg="#ffffff", bd=3, relief="ridge")
result_frame.pack(pady=20, padx=30, fill="both", expand=True)

result_label = tk.Label(
    result_frame, 
    text="", 
    font=("Arial", 16, "bold"), 
    bg="white", 
    fg="#2c3e50", 
    justify="center"
)
result_label.pack(pady=30)

# Run the app
root.mainloop()
