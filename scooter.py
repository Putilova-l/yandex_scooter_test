import requests as requests

import conf
import data


# Функция для создания заказа
def create_orders():
    return requests.post(url=conf.URL + conf.CREATE, json=data.body_create)


# Функция для запроса на получение заказа по треку заказа
def get_orders(track):
    return requests.get(url=conf.URL + conf.GET+"?t="+track)


