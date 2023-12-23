#!/usr/bin/python3

__author__ = "Matteo Golin"

import json
from typing import Pattern
import requests
import re

WEATHER_CODES: dict[str, str] = {
    "113": "☀️ ",
    "116": "⛅",
    "119": "☁️ ",
    "122": "☁️ ",
    "143": "☁️ ",
    "176": "🌧️",
    "179": "🌧️",
    "182": "🌧️",
    "185": "🌧️",
    "200": "⛈️ ",
    "227": "🌨️",
    "230": "🌨️",
    "248": "☁️ ",
    "260": "☁️ ",
    "263": "🌧️",
    "266": "🌧️",
    "281": "🌧️",
    "284": "🌧️",
    "293": "🌧️",
    "296": "🌧️",
    "299": "🌧️",
    "302": "🌧️",
    "305": "🌧️",
    "308": "🌧️",
    "311": "🌧️",
    "314": "🌧️",
    "317": "🌧️",
    "320": "🌨️",
    "323": "🌨️",
    "326": "🌨️",
    "329": "❄️ ",
    "332": "❄️ ",
    "335": "❄️ ",
    "338": "❄️ ",
    "350": "🌧️",
    "353": "🌧️",
    "356": "🌧️",
    "359": "🌧️",
    "362": "🌧️",
    "365": "🌧️",
    "368": "🌧️",
    "371": "❄️",
    "374": "🌨️",
    "377": "🌨️",
    "386": "🌨️",
    "389": "🌨️",
    "392": "🌧️",
    "395": "❄️ ",
}
URL: str = "https://wttr.in/Ottawa"
COLOR_CODES: Pattern[str] = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")


def get_ascii_icon() -> str:
    """Returns just the ASCII icon for the current weather."""
    output = requests.get(URL).text
    lines = output.split("\n")
    icon = "\n".join(lines[2:7])
    return COLOR_CODES.sub("", icon)


def main() -> None:
    weather_data = requests.get(f"{URL}?format=j1").json()["current_condition"][0]
    temperature = weather_data["temp_C"]
    icon = WEATHER_CODES[weather_data["weatherCode"]]

    output = {"text": f"{icon} {temperature}°C", "tooltip": get_ascii_icon()}
    print(json.dumps(output))


if __name__ == "__main__":
    main()
