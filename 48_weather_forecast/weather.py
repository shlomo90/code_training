#-*- encoding: utf-8 -*-

'''
오늘 날씨가 좋은가? 아니면 코트를 들고 나가야 할까?

  http://openweathermap.org/current의 OpenWeatherMap API를
이용하여 도시 이름을 입력하면 입력한 도시의 현재 기온을 나타내는
프로그램을 작성하라.

출력 예
Where are you? Chicago IL
Chicago weather:
65 degrees Fahrenheit

제약 조건
* 날씨를 구하는 부분을 결과를 출력하는 부분과 별도로 분리할 것.

도전 과제
* API는 일출, 일몰 시각뿐만 아니라 습도와 날씨 전망도 제공한다.
  이러한 데이터를 의미 있는 방법으로 나타내도록 프로그램을 수정
  해보자

* API는 풍향을 제공한다. 이 데이터를 "North", "West", "South",
  "South-west" 또는 "South-southwest"와 같은 명칭으로 나타내도록 하라.

* 날씨 프로그램이 오늘이 어떤 날인지 알려주도록 프로그램을 수정해보자.
  가량, 온도가 섭씨 21도이고 하늘이 맑으면 "It's a nice day out!"이라고
  출력한다.

* 기온을 섭씨온도와 화씨온도로 모두 표시하라.

* 날씨 정보를 기반으로 코트 또는 우산이 필요한지 알려주는 프로그램을
  수정해보자



api.openweathermap.org/data/2.5/weather?q={city name},{country code}

Python API

convert_cel_to_feh(cel)
    return feh

get_weather_data(city, code)
    return json file

get_message_of_today(JSON return from get weather data)
get_wind_direction(degree)
    return string 
    
'''


import json
import requests


class InputError(BaseException):
    pass


class OpenWeatherMap(object):
    def __init__(self, **kwargs):
        self.query = ""
        self.request_uri = "http://samples.openweathermap.org/data/2.5/weather"
        self.response = self.send_request(**kwargs)        

        self.weather = json.loads(self.response.text)
        self._report_weather()

    def convert_feh_to_cel(self, feh):
        cel = (float(feh) - 32) / 1.8
        return cel

    def _report_weather(self):
        message = []
        wind = self.weather["wind"]
        message.append("wind is {}".format(wind["speed"]))

        main = self.weather["main"]
        temp = self.convert_feh_to_cel(main["temp"])
        message.append("Temp is {}".format(temp))

        weather = self.weather["weather"][0]
        look = weather["main"]
        direction = self._get_direction(wind["deg"])
        message.append("wind direction is {}".format(direction))


        if look == "Clear" and (temp >=18 and temp <= 22):
            message.append("It's a nice day out!")
        else:
            message.append("Not good")

        print("\n".join(message))
        return message


    def __in_range(self, target, start, end):
        if start > end:
            if ((target >= start and target <= 360.0)
                    or (target >= 0.0 and target <= end)):
                return True
            else:
                return False

        else:
            if target >= start and target <= end:
                return True
            else:
                return False


    def _get_direction(self, deg):
        '''
        Args:
            float type degree.
        Return:
            String Directions(ex: N, NNE, ENE..)
        '''
        deg = float(deg)


        if self.__in_range(deg, 348.75, 11.25):
            direction = "N"
        elif self.__in_range(deg, 11.25, 33.75):
            direction = "NNE"
        elif self.__in_range(deg, 33.75, 56.25):
            direction = "NE"
        elif self.__in_range(deg, 56.25, 78.75):
            direction = "ENE"
        elif self.__in_range(deg, 78.75, 101.25):
            direction = "E"
        elif self.__in_range(deg, 101.25, 123.75):
            direction = "ESE"
        elif self.__in_range(deg, 123.75, 146.25):
            direction = "SE"
        elif self.__in_range(deg, 146.25, 168.75):
            direction = "SSE"
        elif self.__in_range(deg, 168.75, 191.25):
            direction = "S"
        elif self.__in_range(deg, 191.25, 213.75):
            direction = "SSW"
        elif self.__in_range(deg, 213.75, 236.25):
            directino = "SW"
        elif self.__in_range(deg, 236.25, 258.75):
            direction = "WSW"
        elif self.__in_range(deg, 258.75, 281.25):
            direction = "W"
        elif self.__in_range(deg, 281.25, 303.75):
            direction = "WNW"
        elif self.__in_range(deg, 303.75, 326.25):
            direction = "NW"
        else:
            direction = "NNW"
        return direction


    def _set_query(self, value, key=None, mode="a"):
        '''
        Args:
            key: the key of the query
            value: the value of the query
            mode:
                append(a): if self.query has value, It's appended after that
                override(o): use this query even though there are values in
                             self.query.

        Return:
            String: "?<key=value>(&<key=value>)*"
            Set the String to self.query.
        '''

        if key:
            q = "{}={}".format(key, value)
        else:
            q = value

        if self.query:
            if mode == "a":
                if key is None:
                    self.query += ',' + q
                else:
                    self.query += '&' + q
            elif mode == "o":
                if key is None:
                    raise InputError("Key must be needed at this mode")
                else:
                    self.query = q
            else:
                raise InputError("Not support this mode {}".format(mode))
        else:
            self.query = q


    def send_request(self, **kwargs):
        '''
        URL : api.openweathermap.org/data/2.5/weather
        Send The Request URL(above) to get the city's weather data.
        It returns JSON file.
        It could be ignore if no code is put.

        Args:
            city: String (City's Name ex: London)
            code: String (We use ISO 3166 country codes.)

        Return:
            The response which is JSON file of the Request URL.
        '''

        if "cid" in kwargs:
            self._set_query(kwargs["cid"], key="id", mode="o")
        elif "city" in kwargs and "country" in kwargs:
            self._set_query(kwargs["city"], key="q", mode="o")
        elif "zip_code" in kwargs and "country" in kwargs:
            self._set_query(kwargs["zip_code"], key="zip", mode="o")
            self._set_query(kwargs["country"])
        elif "lat" in kwargs and "lon" in kwargs:
            self._set_query(kwargs["lat"], key="lat", mode="o")
            self._set_query(kwargs["lon"], key="lon", mode="a")
        else:
            raise InputError("Arguments Err!, We need at least city, country")

        self._set_query("b6907d289e10d714a6e88b30761fae22", key="appid")

        response = requests.get(self.request_uri + "?" + self.query)
        return response


if __name__ == "__main__":
    w = OpenWeatherMap(cid=168940)

