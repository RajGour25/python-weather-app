
# Python CLI Weather App 🌦️

A command-line Python application built as **Task 03** for my Python Programming Internship at **IncodeVision**. It fetches real-time weather data for any user-specified city using a free weather REST API and displays clean, formatted weather details.

## Features
- **Real-Time Weather Data:** Fetches current temperature, "feels like" temperature, humidity, wind speed, and weather conditions.
- **No API Key Required:** Uses the `wttr.in` JSON endpoint for instant setup and testing.
- **JSON Data Parsing:** Extracts and formats specific weather metrics from structured JSON responses.
- **Error Handling:** Gracefully handles invalid city names, empty inputs, network connection errors, and request timeouts.

## Tech Stack
- **Language:** Python 3
- **Library:** `requests`

The project directory: cd python-weather-app

Install the required dependency: pip install requests

Run the application: python weather_app.py
