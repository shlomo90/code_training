import requests

api_url = 'http://192.168.215.21/prestapi/v2/conf/interface';
data = requests.get(api_url).json();
print(data)
