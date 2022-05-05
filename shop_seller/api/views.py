import requests


def get_a_seat(shrt, long):
    url = f"https://geocode-maps.yandex.ru/1.x/?apikey=a02e49c0-2a47-4a0c-aa6b-87ecea98d282&geocode={long},{shrt}&format=json&results=1"
    data = requests.get(url)
    return(data.text)