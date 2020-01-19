import requests

url = 'https://www.ustc.ac.uk/results?qo=0,0,1&qp=1&qso=11'

response = requests.get(url)

response