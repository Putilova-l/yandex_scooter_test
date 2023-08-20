import scooter

# Путилова Людмила, 7-я когорта — Финальный проект. Инженер по тестированию плюс
# Функция для получения track
def get_new_track():
    # Копируется запрос из файла conf
    #current_track=conf.GET.copy()
    # В переменную get_response сохраняется результат
    get_response = scooter.create_orders()
    # В переменную сохраняется track
    track = get_response.json()["track"]
    return str(track)



# Функция для изменения track в запросе
def get_track_status(track):
    get_response = scooter.get_orders(track)
    return get_response.status_code



# Функция для положительной проверки
def test_success_get_orders_200():
    track = get_new_track()
# В переменную get сохраняется обновлённый запрос
    status=get_track_status(track)
    assert status == 200


