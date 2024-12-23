# Weather App 🌤️

A simple, modern weather application built using Python, Tkinter, and `ttkbootstrap`. The app fetches real-time weather data for any city worldwide using the OpenWeatherMap API and presents it in a visually appealing interface.

---

## Features

- 🌎 **City Search**: Get weather updates for any city around the globe.
- 🌡️ **Weather Details**:
  - Current temperature (in Celsius)
  - Weather description (e.g., sunny, cloudy, rainy)
  - Weather icon representing the conditions
- ⚠️ **Error Handling**: Alerts the user if the city is not found.
- 🎨 **Modern UI**: Styled with `ttkbootstrap` for a sleek and responsive design.

---

## Requirements

- **Python Version**: 3.x
- **Dependencies**:
  - `tkinter` (standard library)
  - `requests` (HTTP requests)
  - `Pillow` (image handling)
  - `ttkbootstrap` (modern UI themes)

Install dependencies with:
```bash
pip install requests pillow ttkbootstrap
```

## Setup Instructions
1. Clone the repository:

```bash
git clone https://github.com/thulanikalatuwawa/WeatherApp
cd WeatherApp
```
2. Obtain an API key from OpenWeatherMap.

3. Replace the placeholder API key in the get_weather() function:
```python
API_key = "your_api_key_here"
```
4. Run the application:
```bash
python WeatherApp.py
```
## How to Use
1. Launch the app.
2. Enter a city name in the input field.
3. Click Search.
4. View the weather details, including:
- City and country
- Current temperature
- Weather description
- Icon representing the conditions

##Preview
Main Interface

Weather Result Example

## Project Structure
```
WeatherApp/
├── WeatherApp.py    # Main application script
├── README.md         # Project documentation

```

## Limitations
- Requires an active internet connection to fetch weather data.
- The app uses the free tier of OpenWeatherMap, which has API call limits.

##License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
- OpenWeatherMap for their comprehensive weather API.
- ttkbootstrap for providing modern Tkinter themes.
- Python and its fantastic community!

## Contributing
Feel free to fork this repository, make improvements, and submit a pull request! Contributions are welcome.

