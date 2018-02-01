'''
hello!
This is a code for getting weather.!
'''
import requests

api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1';
payload = {"city":"130010"};
weather_data = requests.get(api_url, params = payload).json();
print(weather_data['forecasts'][0]['dateLabel'] + 'weather is' + weather_data
      ['forecasts'][0]['telop'])


