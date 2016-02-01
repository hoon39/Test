import urllib.request as MyURL

response = MyURL.urlopen('http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109')

print(response)