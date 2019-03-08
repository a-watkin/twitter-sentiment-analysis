import yweather

"""
uses yahoo api call to get country code
"""
client = yweather.Client()
print(client.fetch_woeid('Finland'))
