import requests

"""
The `requests` module in Python is a popular HTTP library for making network requests. It simplifies sending HTTP/1.1 requests, handling responses, and managing sessions. Key features include:

- Sending HTTP requests (GET, POST, PUT, DELETE, etc.) with simple function calls.
- Handling query parameters, form data, JSON payloads, and file uploads.
- Managing cookies and sessions for persistent connections.
- Automatic decoding of response content and support for custom headers.
- Exception handling for network errors and timeouts.
- SSL verification and proxy support.
"""
# Real-life example: Fetching current weather data from OpenWeatherMap API

api_key = "your_api_key_here"
city = "London"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Raises HTTPError for bad responses
    data = response.json()
    print(
        f"Weather in {city}: {data['weather'][0]['description']}, Temperature: {data['main']['temp']}°C"
    )
except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")
