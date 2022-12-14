#coding=utf-8
import unittest
import requests
from time import sleep
import urllib.parse
import json

class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.url='https://free-api.heweather.net/s6/weather/now?'

    def test_weather_beijing(self):
        data={'location':'北京','key':'b1b5eaba002b43d5ada566c424928d78'}
        r=requests.get(self.url,params=data)
        result=r.json()

        self.assertEqual(result['HeWeather6'][0]['status'], 'ok')
        self.assertEqual(result['HeWeather6'][0]['basic']['cid'], 'CN101010100')

    def test_weather_nonlocation(self):
        data = {'key': 'b1b5eaba002b43d5ada566c424928d78'}
        r = requests.get(self.url, params=data)
        result = r.json()

        self.assertEqual(result['HeWeather6'][0]['status'], 'invalid param')


if __name__=='__main__':
    unittest.main()
