# Luna is a simple AQI Discord bot.

AQI is Air Quality Index (basically a measurement of how polluted the air is)

Currently all Luna does (when online) is leverage the [aqicn.org](https://aqicn.org/) API to respond to two slash commands:

`/aqi {city}` Takes a string argument to search for the AQI measurement of a city.


 `/aqi_all` Gathers the AQI reading of a list of hard-coded locations where I am personally invested in knowing the air quality of.


A visual element that LunaBot adds is adding circle emojis of the color corresponding to the AQI reading.