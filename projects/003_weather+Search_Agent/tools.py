from langchain_nimble import NimbleSearchTool
from langchain.tools import tool
import os
import requests


search_tool = NimbleSearchTool(
    k = 5,
    deep_search = True,
    parsing_type="markdown"
)

@tool
def google_search(query:str):
    """
    Search anything on google for real time information.
    Args:
        query - user search query for google search
        
    Return - result from google search
    """
    res = search_tool.invoke(query)
    return res


@tool
def weather_tool(city:str):
    """
        Get real time weather details like temperature, humidity and others.
        Args:
            city - city name for weather details
        Return -> Weather data from the api response.
    """
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not api_key:
        return "OpenWeatherMap is not configured. Set OPENWEATHERMAP_API_KEY in .env."

    res = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"q": city, "appid": api_key},
        timeout=10,
    )
    if res.status_code == 200:
        return res.json()
    
    return "Unable to find details for this city"


ALL_TOOLS = [google_search, weather_tool]